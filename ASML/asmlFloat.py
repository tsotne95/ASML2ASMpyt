from .asmlFunDef import asmlFunDef
from .operType import operType
from .asmlOper import asmlOper

class asmlFloat(asmlFunDef):
    def __init__(self,instruction):
        data=instruction.split(" ")
        self.op=asmlOper(data[1],operType.VAR)
        self.value=None
    
    def __str__(self):
        return "FLOAT : let " + str(self.op) + " = " + str(self.value) + "\n"

    def generateAsm(self):
        return "FLOAT NOT YET IMPLEMENTED\n"
