# ASML2ASMpyt
ASML2ASMpyt generate ARM Assembly from asml, which is intermediate format from minCaml language.

```bash
usage: main.py [-i] [-f file] [-io file] [-fo]
-i       -- read asml data from standard input, generate asm to standard output
-f file  -- read asml data from .asml file, generate asm to standard output
-io file -- read asml data from standard input, generate asm in argument file
-fo file file -- read asml .asml file, generate asm to outputFile
```
For register allocation we used basic allocation strategy (spill) with kind of policies:
1. The registers used by the parameters are the registers from r0 to r3.
   so, if there are more than 4 parameters, the parameters are put on the stack.
2. The last instruction of the function saves the result in r0.
3. If there are strictly less than 8 local variables, we use all the registers from r5 to r10 to save them.
   Otherwise, we use the registers from r5 to r8 for the first 5 variables, and the other variables go to the stack, and we use r9 and r10 to load them when necessary.
4. r12 contains the result of an expression.
5. r11 is the frame pointer.
6. r4 serves as a heap pointer.

LABELs and FLOATs not yet implemented.

Python is cool and at nearly 6am, I feel as python GURU :sunglasses:
