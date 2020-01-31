from .asmlExp import asmlExp
from .operType import operType
from .asmlOper import asmlOper
from .asmlBranch import asmlBranch
import re

class asmlIf(asmlBranch,asmlExp):
    def __init__(self, instruction):
        asmlBranch.__init__(self)
        asmlIf.areInIf=True
        self.exLabel=None
        self.constructionThen=True #to indicate if we are in the then or else
        data=instruction.split(" ")
        optype=None
        if re.match(r'[0-9]+',data[1]) is not None:
            optype=operType.IMM
        else:
            optype=operType.VAR
        self.op1=asmlOper(data[1],optype)
        self.comparator=data[2]
        optype=None
        if re.match(r'[0-9]+',data[3]) is not None:
            optype=operType.IMM
        else:
            optype=operType.VAR
        self.op2=asmlOper(data[3],optype)
        self.expThen=[]
        self.expElse=[]

    def addInstruction(self,expression):
        #print(self.constructionThen,expression)
        if self.constructionThen:
            self.expThen.append(expression)
        else:
            self.expElse.append(expression)
    
    def setConstructionThen(self,constructionThen):
        self.constructionThen = constructionThen

    def getOpers(self):
        a = []
        a.append(self.op1)
        a.append(self.op2)
        for exp in self.expThen:
            a=a+exp.getOpers()
        
        for exp in self.expElse:
            a=a+exp.getOpers()

        return a

    def getOpersCon(self,type):
        a = []
        if self.op1.getType()==type:
            a.append(self.op1)

        if self.op2.getType()==type:
            a.append(self.op2)

        for exp in self.expThen:
            a=a+exp.getOpersCon(type)
        
        for exp in self.expElse:
            a=a+exp.getOpersCon(type)
            
        return a

    def generateAsm(self):
        #if
        code = ""
        if self.op1.getName().startswith("r") and self.op2.getName().startswith("r"): #everything is in the registers
            code += "\tcmp " + str(self.op1) + ", " + str(self.op2) + "\n"
        else:
            if not self.op1.getName().startswith("r") and not self.op2.getName().startswith("r"): #op1 and op2 must be loaded into the register
                if self.op1.isVariable():
                    code += "\tldr r9, " + str(self.op1) + "\n"
                else: # immediate value
                    code += "\tldr r9, =#" + str(self.op1) + "\n"

                if self.op2.isVariable():
                    code += "\tldr r10, " + str(self.op2) + "\n"
                else: # immediate value
                    code += "\tldr r10, =#" + str(self.op2) + "\n"
                
                code += "\tcmp r9, r10\n"
            elif not self.op1.getName().startswith("r"): #op1 must be loaded into memory
                if self.op1.isVariable():
                    code += "\tldr r9, " + str(self.op1) + "\n"
                else: #immediate value
                    code += "\tldr r9, =#" + str(self.op1) + "\n"  
                code += "\tcmp r10, " + str(self.op2) + "\n"
            else: #op2 must be loaded into memory
                if self.op2.isVariable():
                    code += "\tldr r10, " + str(self.op2) + "\n"
                else: #immediate value
                    code += "\tldr r10, =#" + str(self.op2) + "\n"
                code += "\tcmp " + str(self.op1) + ", r10\n"
        
        #floats are not yet managed
        if self.comparator=="=":
            code += "\tbne LAB_E_" + str(id(self)) + "\n"
        elif self.comparator=="<=":
            code += "\tbgt LAB_E_" + str(id(self)) + "\n"
        elif self.comparator=="<":
            code += "\tbge LAB_E_" + str(id(self)) + "\n"
        elif self.comparator==">=":
            code += "\tblt LAB_E_" + str(id(self)) + "\n"
        elif self.comparator==">":
            code += "\tble LAB_E_" + str(id(self)) + "\n"

        #then
        code += "LAB_T" + str(id(self)) + ":\n"

        for exp in self.expThen:
            code += exp.generateAsm()
        
        self.exLabel="lab_ex"+str(id(self))

        code += "\tb "+self.exLabel+"\n"

        code += "LAB_E_" + str(id(self)) + ":\n"
        for exp in self.expElse:
            #print(exp)
            code += exp.generateAsm()
        code += "\tb "+self.exLabel+"\n"

        return code