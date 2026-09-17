# Public-edition execution records

`public-edition-final/` is the replay of the assembled edition with frozen inputs. Its `execution.json` reports each command's exit code, effective resource caps, output hashes and before/after source hashes. A completed zero-exit mathematical check and an unchanged input snapshot are both required for the runner's final pass. The same execution record is available at `../PUBLIC_REPLAY.json` for an immediate machine-readable entry point.
