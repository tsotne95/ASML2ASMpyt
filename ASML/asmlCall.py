from .asmlExp import asmlExp
from .operType import operType
from .asmlOper import asmlOper
import re

class asmlCall(asmlExp):

    def __init__(self,instruction):
        data=instruction.split(" ")
        self.funcLabel=data[1]
        self.params=[]
        for i in range(2,len(data)):
            optype=None
            if re.match(r'[0-9]+',data[i]) is not None:
                optype=operType.IMM
            else:
                optype=operType.VAR
            p=asmlOper(data[i],optype)
            self.params.append(p)
    
    def getOpers(self):
        return self.params
    
    def getOpersCon(self,type):
        a=[]
        for op in self.params:
            if op.getType()==type:
                a.append(op)
        return a
    def __str__(self):
        res = "call " + self.funcLabel
        for p in self.params:
            res += " " + str(p)
        return res

    def generateAsm(self):
        code=""
        #save registers r0-r3
        code += "\tpush {r0-r3}\n"
        #parameters
        for i in range(0,len(self.params)):
            p=self.params[i]
            if i<4: #we load them in the registers r0-r3
                if p.isVariable():
                    if p.getName().startswith("r"): # register
                        code += "\tmov r" + str(i) + ", " + p.getName() + "\n"
                    else: #stack
                        code += "\tldr r" + str(i) + ", " + p.getName() + "\n"
                else: #immediate value
                    code += "\tldr r" + str(i) + ", =#" + p.getName() + "\n"
            else: #otherwise into stack
                if p.isVariable():
                    if p.getName().startswith("r"): #register
                        code += "\tpush {" + p.getName() + "}\n"
                    else: #stack
                        code += "\tldr r12, sp, " + p.getName() + "\n"
                        code += "\tpush {r12}\n"
                else: # immediate value
                    code += "\tldr r12, =#" + p.getName() + "\n"
                    code += "\tpush {r12}\n"
        #calling
        code += "\tbl " + self.funcLabel + "\n"
        #restoration
        code += "\tpop {r0-r3}\n"
        return code
