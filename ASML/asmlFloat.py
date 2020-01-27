from .asmlFunDef import asmlFunDef
from .operType import operType
from .asmlOper import asmlOper


class asmlFloat(asmlFunDef):
    def __init__(self, instruction):
        data = instruction.split(" ")
        self.op = asmlOper(data[1], operType.VAR)
        self.value = self.IEEE754(float(data[3]))

    def __str__(self):
        return "FLOAT : let " + str(self.op) + " = " + str(self.value) + "\n"

    def generateAsm(self):
        return "FLOAT NOT YET IMPLEMENTED\n"


    def float_bin(self,number, places=3):
        whole, dec = str(number).split(".")
        whole = int(whole)
        dec = int(dec)
        res = bin(whole).lstrip("0b") + "."

        for x in range(places):
            whole, dec = str((self.decimal_converter(dec)) * 2).split(".")
            dec = int(dec)
            res += whole
        return res


    def decimal_converter(self,num):
        while num > 1:
            num /= 10
        return num


    def IEEE754(self,n):
        sign = 0
        if n < 0:
            sign = 1
            n = n * (-1)
        p = 30

        dec = self.float_bin(n, places=p)

        whole, dec = str(dec).split(".")
        whole = int(whole)

        exponent = len(str(whole)) - 1
        exponent_bits = 127 + exponent
        exponent_bits = bin(exponent_bits).lstrip("0b")

        mantissa = str(whole)[1:exponent + 1]
        mantissa = mantissa + dec
        mantissa = mantissa[0:23]

        final = str(sign) + str(exponent_bits) + mantissa

        hstr = '%0*X' % ((len(final) + 3) // 4, int(final, 2))
        return (hstr)
