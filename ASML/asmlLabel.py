from .asmlFunDef import asmlFunDef
from .operType import operType
from .asmlOper import asmlOper
from .asmlExp import asmlExp

class asmlLabel(asmlExp):
    def __init__(self,instruction):
        self.name = instruction

    def getOpers(self):
        return []

    def getOpersCon(self,type):
        return []

    def __str__(self):
        return self.name

    def generateAsm(self):
        return "LABEL NOT YET IMPLEMENTED\n"