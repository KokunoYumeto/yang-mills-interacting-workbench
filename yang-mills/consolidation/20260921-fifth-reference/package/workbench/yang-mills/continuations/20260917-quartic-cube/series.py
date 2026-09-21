"""Exact constants and rational enclosures; physical parameters are unchanged."""
from fractions import Fraction as F
from math import isqrt

A3=F(918680,351)
M3=F(336572872,208845)
T3=F(225985217,1253070)
A4=F(2296826751679,30073680)
M2=F(5834,39);T2=F(137,6)
L3=M3+4*T3
B23=3*(M2*T3+M3*T2)
B33=6*M3*T3
P3=3*M3/2-6*T3

def ell(x):return F(128,3)*x+F(3132,13)*x*x+L3*x**3
def delta(x):return A4*x**4+2*B23*x**5+B33*x**6
def disc(x):return (1-ell(x))**2-F(8,3)*delta(x)
def square_root_box(x,digits=60):
    x=F(x)
    if x<0:raise ValueError('negative radicand')
    den=10**digits;k=isqrt(x.numerator*den*den//x.denominator)
    lo,hi=F(k,den),F(k+1,den)
    if not lo*lo<=x<hi*hi:raise ArithmeticError('square root enclosure')
    return lo,hi

def root_box():
    lo,hi=F(178,10000),F(179,10000)
    if not disc(lo)>0>disc(hi) or not ell(hi)<1:raise ArithmeticError('root sign')
    for _ in range(140):
        mid=(lo+hi)/2
        if disc(mid)>0:lo=mid
        else:hi=mid
    return lo,hi

def gap_box(x):
    sl,sh=square_root_box(disc(x))
    p=F(1136,13)*x*x+P3*x**3
    return F(3,2)*(1+sl)+p,F(3,2)*(1+sh)+p

def correction_box(x):
    sl,sh=square_root_box(disc(x))
    return F(3,4)*(1-ell(x)-sh),F(3,4)*(1-ell(x)-sl)

M4=F(17270702970768271,341697152160)
T4=F(110695177857394584026401,18025447358750832000)
L4=M4+4*T4
B14=3*(F(64,3)*T4+M4*F(16,3))
B24=3*(M2*T4+M4*T2)
B34=3*(M3*T4+M4*T3)
B44=6*M4*T4
P4=3*M4/2-6*T4

def ell_quartic(x):return ell(x)+L4*x**4
def delta_quartic(x):return (2*B14+2*B23)*x**5+(2*B24+B33)*x**6+2*B34*x**7+B44*x**8
def disc_quartic(x):return (1-ell_quartic(x))**2-F(8,3)*delta_quartic(x)
def root_quartic_box():
    lo,hi=F(181,10000),F(182,10000)
    if not disc_quartic(lo)>0>disc_quartic(hi) or not ell_quartic(hi)<1:raise ArithmeticError('quartic reference root sign')
    for _ in range(140):
        mid=(lo+hi)/2
        if disc_quartic(mid)>0:lo=mid
        else:hi=mid
    return lo,hi

def gap_quartic_box(x):
    a,b=square_root_box(disc_quartic(x));p=F(1136,13)*x*x+P3*x**3+P4*x**4
    return F(3,2)*(1+a)+p,F(3,2)*(1+b)+p

def correction_quartic_box(x):
    a,b=square_root_box(disc_quartic(x))
    return F(3,4)*(1-ell_quartic(x)-b),F(3,4)*(1-ell_quartic(x)-a)
