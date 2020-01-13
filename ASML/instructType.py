import enum
import re

class instructType(enum.Enum):
    NOP=1
    INT=2
    IDENT=3
    LABEL=4
    NEG=5
    FNEG=6
    FADD=7
    FSUB=8
    FMUL=9
    FDIV=10
    NEW=11
    ADD=12
    SUB=13
    MEM=14
    IF=15
    FI=16
    ELSE=17
    CALL=18
    CALLCLO=19
    LET_IN=20
    LET_FLOAT=21
    LET_FUN=22

    @classmethod
    def getTypeInstruction(cls,instr):
        instr=instr+"   " #or the substr/ it doesn't crash if it's short
        instrSub=instr[0:3]
        if instrSub=="nop":
            return cls.NOP
        elif instrSub=="neg":
            return cls.NEG
        elif instrSub=="fne":
            return cls.FNEG
        elif instrSub=="fad":
            return cls.FADD
        elif instrSub=="fsu":
            return cls.FSUB
        elif instrSub=="fdi":
            return cls.FDIV
        elif instrSub=="new":
            return cls.NEW
        elif instrSub=="add":
            return cls.ADD
        elif instrSub=="sub":
            return cls.SUB
        elif instrSub=="mem":
            return cls.MEM
        elif instrSub=="if ":
            return cls.IF
        elif instrSub==") e":
            instrTr=instr.strip()
            if instrTr==") else (":
                return cls.ELSE
            else:
                return None
        elif instrSub=="cal":
            return cls.CALL
        elif instrSub=="app":
            return cls.CALLCLO
        elif instrSub=="let":
            if instr.startswith("let _"):
                instrTr=instr.strip()
                if instrTr.endswith("="):
                    return cls.LET_FUN
                else:
                    return cls.LET_FLOAT
            else:
                return cls.LET_IN
        else:
            if re.match(r'[0-9]+\s*',instr) is not None:
                return cls.INT
            elif re.match(r'[a-z0-9]+\s*',instr) is not None:
                return cls.IDENT
            elif instr.startswith("_"):
                return cls.LABEL
            elif instr.startswith("("):
                instrSubstr=instr[1:len(instr)-2]
                instrSubstr=instrSubstr.strip()
                return cls.getTypeInstruction(instrSubstr)
            elif instr.startswith(")"):
                return cls.FI
            else:
                return cls.NOP
