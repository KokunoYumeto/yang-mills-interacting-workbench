# Execution diagnostics retained

A source-corruption CLI test expected FAIL: predecessor-hash:verify.py; the checker instead rejected with exit1 and an uncaught pre-main ValueError bearing that same exact code.

Catch the explicit source-pin ValueError/OSError before import and emit the same named FAIL line with exit1. Regenerate and replay the complete final receipt.

Diagnostic guard only; no mathematical statement, tested formula, source pin or validation rule changed.

Earlier outer harness attempts reached their execution limit without a complete receipt; they are not counted as passed. The final complete finite replay returned exit0 and produced execution.json. All spawned replay processes have finished.

Earlier checker SHA-256: `45bc148e184b95e35f214bd9fe71f80b58aebc5fa0db7bb82462a35c6689d766`.
Final checker SHA-256: `d78432d5eeab097efa7aa018de30932d67c4c77edcc4ceeeae843b955f60f655`.
