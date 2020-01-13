import re
class asml:
    def __init__(self,code):
        self.labels={}
        self.generateLabels(code)
        self.immediateOptim()
        self.allocRegSpill()
        self.generateAsm()
    
    def generateLabels(self,code):
        self.labels={}
        lines=code.splitlines()
        label=''
        for instr in lines:
            instr=instr.strip()
            if re.match(r'let _[a-z0-9_]* =[ 0-9.]*',instr) is not None: #label (= float or func)
                start=instr.index('let _')+4
                end=instr.index('=')-1
                label=instr[start:end]
                self.labels[label]=[]
                instr=instr.strip()
                if not instr.endswith('='): #func
                    self.labels[label].append(instr)
                else:
                    if not (instr==')' or instr==''):
                        if label in self.labels:
                            self.labels[label].append(instr)
                        else:
                            assert(False)
    
    def immediateOptim(self):
        pass

    def allocRegSpill(self):
        pass
    
    def generateAsm(self):
        pass

    def printLabels(self):
        for key,value in self.labels:
            print("LABEL : " + key)
            for s in value:
                print(s)
