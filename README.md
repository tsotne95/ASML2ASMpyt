# ASML2ASMpyt
ASML2ASMpyt generate ARM Assembly from asml, which is intermediate format from minCaml language.

```bash
usage: main.py [-i] [-f file] [-io file] [-fo]
-i       -- read asml data from standard input, generate asm to standard output
-f file  -- read asml data from .asml file, generate asm to standard output
-io file -- read asml data from standard input, generate asm in argument file
-fo file -- read asml .asml file, generate asm to file.s, in same directory
```
