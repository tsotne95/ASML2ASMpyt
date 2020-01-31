from .instructType import instructType
from .asmlCall import asmlCall
from .asmlNew import asmlNew
from .asmlMem import asmlMem
from .asmlArithmetics import asmlArithmetics
from .asmlLabel import asmlLabel
from .asmlBranch import asmlBranch
from .asmlFunc import asmlFunc
from .asmlFloat import asmlFloat
from .asmlIf import asmlIf
from .asmlLet import asmlLet
from .asmlFunDef import asmlFunDef

class asmlTree:
    def __init__(self,code):
        self.labels=[]
        instructions=code.splitlines()
        currentBranch=asmlBranch() 
        
        for instr in instructions:
            currentBranch=self.decoderInstruction(instr,currentBranch)

    def decoderInstruction(self, instruction,currentBranch):
        instruction=instruction.strip()
        instrType=instructType.getTypeInstruction(instruction)

        #print(currentBranch,instruction,instrType)

        if instrType==instructType.LET_FUN:
            a_fun=asmlFunc(instruction)
            self.labels.append(a_fun)
            currentBranch=a_fun
        elif instrType==instructType.LET_FLOAT:
            a_float=asmlFloat(instruction)
            self.labels.append(a_float)
        elif instrType==instructType.IF:
            a_if=asmlIf(instruction)
            currentBranch.addInstruction(a_if)
            tmp=currentBranch
            currentBranch=a_if
            currentBranch.setParent(tmp)
        elif instrType==instructType.ELSE:
            currentBranch.setConstructionThen(False)
        elif instrType==instructType.FI:
            currentBranch=currentBranch.getParent()
        elif instrType==instructType.LET_IN:
            a_let=asmlLet(instruction)
            #print("uuuuu\n",a_let,"\naaaaaaaaa")
            currentBranch.addInstruction(a_let)
        elif instrType==instructType.ADD:
            a_arith=asmlArithmetics(instruction)
            currentBranch.addInstruction(a_arith)
        elif instrType==instructType.SUB:
            a_arith=asmlArithmetics(instruction)
            currentBranch.addInstruction(a_arith)
        elif instrType==instructType.FADD:
            a_arith=asmlArithmetics(instruction)
            currentBranch.addInstruction(a_arith)
        elif instrType==instructType.FSUB:
            a_arith=asmlArithmetics(instruction)
            currentBranch.addInstruction(a_arith)
        elif instrType==instructType.CALL:
            a_call=asmlCall(instruction)
            currentBranch.addInstruction(a_call)
        elif instrType==instructType.NOP:
            pass
        elif instrType==instructType.MEM:
            a_mem=asmlMem(instruction)
            currentBranch.addInstruction(a_mem)
        return currentBranch

    def registerAllocation_Spill(self):
        for label in self.labels:
            #print("start\n",label,"end\n",isinstance(label,asmlFunc))
            if isinstance(label,asmlFunc):
                #parameters
                label.allocRegSpill()
    
    def generateAsm(self):
        code = ""
        code += "\t.text\n"
        code += "\t.global _start\n"
        for a in self.labels:
            code += a.generateAsm()
        return code
    
    def __str__(self):
        res = "-------- TREE ----------\n"
        for a in self.labels:
            res += str(a)
        return res
