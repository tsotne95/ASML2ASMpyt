class asmlBranch:
    def __init__(self):
        self.parent=None

    def addInstruction(self,expression):
        pass

    def getParent(self):
        return self.parent

    def setParent(self,parent):
        self.parent = parent