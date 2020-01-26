from .asmlExp import asmlExp
from .operType import operType
from .asmlOper import asmlOper
import re

class asmlNew(asmlExp):
    def __init__(self,exp):
        data=exp.split(" ")
        data=data[1]
        optype=None
        if re.match(r'[0-9]+',data) is not None:
            optype=operType.IMM
        else:
            optype=operType.VAR
        self.op=asmlOper(data,optype)
    
    def getOpers(self):
        a=[]
        a.append(self.op)
        return a

    def getOpersCon(self,type):
        a=[]
        if self.op.getType==type:
            a.append(self.op)
        return a
    
    def __str__(self):
        return "new " + str(self.op)

    def generateAsm(self):
        code = ""
        code += "\tldr r12, [r4]\n" #allows to return the allocation start address
        code += "\tsub r4, r4, #" + str(self.op) + "\n" #moving the heap pointer
        return code