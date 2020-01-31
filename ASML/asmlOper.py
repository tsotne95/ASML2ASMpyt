from .asmlExp import asmlExp
from .operType import operType

class asmlOper(asmlExp):
    def __init__(self,name,type):
        self.name=name #name if variable / value if immediate value
        self.type=type

    def getName(self):
        return self.name
    
    def isVariable(self):
        return self.type==operType.VAR

    def getType(self):
        return self.type
    
    def renameVariable(self, newName):
        self.name = newName

    def __str__(self):
        return self.name

    def getOpers(self):
        a=[]
        a.append(self)
        return a

    def getOpersCon(self,type):
        a=[]
        if self.type==type:
            a.append(self)
        return a

    def generateAsm(self):
        if self.name.startswith("r"):
            return "\tmov r12, " + self.name + "\n"
        else: #manage it if immediate value or save it in memory
            if self.name.startswith("["): #memory
                data=[]
                nameRep=self.name.replace("[","")
                nameRep=nameRep.replace("]","")
                data=nameRep.split(", ")
                return "\tldr r12, " + self.name + "\n"
            else: #immediate value
                imVal=self.name.split(" ")
                imVal=imVal[0]
                return "\tldr r12, =#" + imVal + "\n"
