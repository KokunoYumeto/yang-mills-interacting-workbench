"""Independent finite check of cube orders and open-box counts; no producer imports.

Single Python worker, Windows process memory cap 1 GiB and one CPU affinity.
The mathematical input is a unit cube or open box [0,m]^3, m=2,...,8.
Face edges are unordered endpoint pairs. No source transcript is executed.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import combinations, permutations, product
from time import perf_counter
import ctypes
from ctypes import wintypes as w
import hashlib
import json
from pathlib import Path
import platform


def enforce_resources():
    class Basic(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_int64), ("job_time", ctypes.c_int64),
                    ("flags", w.DWORD), ("min_ws", ctypes.c_size_t),
                    ("max_ws", ctypes.c_size_t), ("active", w.DWORD),
                    ("affinity", ctypes.c_size_t), ("priority", w.DWORD),
                    ("scheduling", w.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_uint64) for name in
                    ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]
    class Extended(ctypes.Structure):
        _fields_ = [("basic", Basic), ("io", IO), ("process_memory", ctypes.c_size_t),
                    ("job_memory", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                    ("peak_job", ctypes.c_size_t)]
    k = ctypes.WinDLL("kernel32", use_last_error=True)
    k.GetCurrentProcess.restype = w.HANDLE
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, w.LPCWSTR]
    k.CreateJobObjectW.restype = w.HANDLE
    k.SetInformationJobObject.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    k.AssignProcessToJobObject.argtypes = [w.HANDLE, w.HANDLE]
    k.GetProcessAffinityMask.argtypes = [w.HANDLE, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_size_t)]
    k.SetProcessAffinityMask.argtypes = [w.HANDLE, ctypes.c_size_t]
    job = k.CreateJobObjectW(None, None)
    limits = Extended()
    limits.basic.flags = 0x100 | 0x8  # process memory and active-process caps
    limits.basic.active = 1
    limits.process_memory = 1024**3
    proc = k.GetCurrentProcess()
    if not job or not k.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not k.AssignProcessToJobObject(job, proc):
        raise ctypes.WinError(ctypes.get_last_error())
    pmask, smask = ctypes.c_size_t(), ctypes.c_size_t()
    if not k.GetProcessAffinityMask(proc, ctypes.byref(pmask), ctypes.byref(smask)):
        raise ctypes.WinError(ctypes.get_last_error())
    cpu = pmask.value & -pmask.value
    if not k.SetProcessAffinityMask(proc, cpu):
        raise ctypes.WinError(ctypes.get_last_error())
    return job, {"memory_bytes": 1024**3, "active_processes": 1, "affinity_mask": cpu}


def face_edges(origin, axes):
    i, j = axes
    points = []
    for a, b in ((0, 0), (1, 0), (1, 1), (0, 1)):
        p = list(origin)
        p[i] += a
        p[j] += b
        points.append(tuple(p))
    return frozenset(tuple(sorted((points[z], points[(z+1) % 4]))) for z in range(4))


def faces(m):
    result = []
    for axes in combinations(range(3), 2):
        ranges = [range(m) if a in axes else range(m+1) for a in range(3)]
        for origin in product(*ranges):
            result.append(face_edges(origin, axes))
    assert len(set(result)) == len(result)
    return result


def cube_orders():
    cube = faces(1)
    assert len(cube) == 6 and len(set().union(*cube)) == 12
    hist = Counter()
    exact = F(0)
    for order in permutations(range(6)):
        boundary = set()
        lengths = []
        denominator = F(1)
        for face in order[:-1]:
            boundary.symmetric_difference_update(cube[face])
            lengths.append(len(boundary))
            assert boundary
            denominator *= F(4, 3*len(boundary))
        hist[tuple(lengths)] += 1
        exact += denominator
        boundary.symmetric_difference_update(cube[order[-1]])
        assert not boundary
    expected = {(4,8,8,8,4):48, (4,8,8,6,4):96, (4,6,8,8,4):96,
                (4,6,8,6,4):192, (4,6,6,6,4):288}
    assert dict(hist) == expected and sum(hist.values()) == 720
    assert exact == F(166,243)
    assert -exact*F(1,16) == F(-83,1944)
    triples = Counter()
    three_plus_three = F(0)
    for subset in combinations(range(6), 3):
        degree_sum = sum(bool(cube[a] & cube[b]) for a,b in combinations(subset,2))
        boundary = set()
        for p in subset:
            boundary.symmetric_difference_update(cube[p])
        if degree_sum == 2:
            triples["path"] += 1
            c = F(3,4)*len(boundary)
            a = (F(1,9)+F(4,27)+F(4,27))/c
            assert c == 6 and a == F(11,162)
        else:
            assert degree_sum == 3
            triples["corner"] += 1
            c = F(3,4)*len(boundary)
            a = (3*F(4,27))/c
            assert c == F(9,2) and a == F(8,81)
        three_plus_three -= F(1,16)*c*a*a
    assert triples == {"path":12,"corner":8}
    assert three_plus_three == F(-83,1944)
    return {"orders":720, "histogram":[[list(key), hist[key]] for key in sorted(hist)],
            "resolvent_sum":str(exact), "haar_factor":"1/16", "cube_energy":str(-exact/16),
            "three_face_subsets":dict(triples),"three_plus_three_energy":str(three_plus_three)}


def count_box(m):
    fs = faces(m)
    incident = defaultdict(set)
    for p, edges in enumerate(fs):
        for edge in edges:
            incident[edge].add(p)
    adjacent = [set().union(*(incident[e] for e in edges)) - {p} for p, edges in enumerate(fs)]
    pairs = sum(map(len, adjacent)) // 2
    wedges = sum(len(neighbors)*(len(neighbors)-1)//2 for neighbors in adjacent)
    triangles = set()
    for p, neighbors in enumerate(adjacent):
        for q, r in combinations(sorted(neighbors),2):
            if q in adjacent[r]:
                triangles.add(tuple(sorted((p,q,r))))
    common = sum(bool(fs[a] & fs[b] & fs[c]) for a,b,c in triangles)
    corners = len(triangles)-common
    paths = wedges-3*len(triangles)
    actual = [len(fs), pairs, paths, common, corners, m**3, wedges]
    expected = [3*m*m*(m+1), 6*m*(3*m*m-1), 138*m**3-126*m*m-24*m+12,
                12*m*m*(m-1),8*m**3,m**3,198*m**3-162*m*m-24*m+12]
    assert actual == expected, (m,actual,expected)
    return {"m":m, "M,J,P,T,C,B,wedges":actual}


def polynomial_check():
    # Increasing powers of m; each row is exactly the stated support count.
    polys = [[0,0,3,3], [0,-6,0,18], [12,-24,-126,138], [0,0,-12,12],
             [0,0,0,8], [0,0,0,1]]
    weights = [F(-289,77760),F(22285,23654592),F(-4909,118272960),
               F(244,4312035),F(-212,542997),F(-83,1944)]
    result = [sum(weights[i]*polys[i][k] for i in range(6)) for k in range(4)]
    expected = [F(-n,4691494080) for n in (2336684,21845782,30959193,211396463)]
    assert result == expected
    at_m4 = sum(result[k]*4**k for k in range(4))
    assert at_m4 == F(-3528610133,1172873520)
    plaquette_cubic = -2*(F(5,216)-F(2,1053)*6)
    plaquette_quintic = -result[3]
    assert plaquette_cubic == F(-11,468)
    assert plaquette_quintic == F(211396463,4691494080)
    return {"e6_m_polynomial_ascending":[str(x) for x in result], "e6_m4":str(at_m4),
            "plaquette_cubic":str(plaquette_cubic),"plaquette_quintic":str(plaquette_quintic)}


if __name__ == "__main__":
    started_at = datetime.now(timezone.utc).isoformat()
    started = perf_counter()
    job_handle, limits = enforce_resources()
    result = {"cube":cube_orders(), "boxes":[count_box(m) for m in range(2,9)],
              "polynomial":polynomial_check(), "resource_limits":limits,
              "python":platform.python_version(),"worker_count":1,
              "started_at":started_at,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result["runtime_seconds"] = perf_counter()-started
    print(json.dumps(result, indent=2))
