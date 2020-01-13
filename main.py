#!/usr/bin/python3
import sys
import argparse
import os
from ASML import asmlTree

def main():
    
    if len(sys.argv)<2:
        sys.exit("Insufficient arguments")
    if sys.argv[1]=='-h':
        print("usage: main.py [-i] [-f file] [-io file] [-fo]")
        print("-i       -- read asml data from standard input, generate asm to standard output")
        print("-f file  -- read asml data from .asml file, generate asm to standard output")
        print("-io file -- read asml data from standard input, generate asm in argument file")
        print("-fo file -- read asml .asml file, generate asm to file.s, in same directory")
    elif sys.argv[1]=='-i':
        data=""
        for line in sys.stdin:
            data+=line
        t=asmlTree.asmlTree(data)
        t.registerAllocation_Spill()
        #print(t) #to print AST uncoment this line
        print(t.generateAsm())
    elif sys.argv[1]=='-f':
        if len(sys.argv)<3:
            sys.exit("Insufficient arguments")
        else:
            with open(sys.argv[2],'r') as file:
                data=file.read()
            t=asmlTree.asmlTree(data)
            t.registerAllocation_Spill()
            #print(t) #to print AST uncoment this line
            print(t.generateAsm())
    elif sys.argv[1]=='-io':
        if len(sys.argv)<3:
            sys.exit("Insufficient arguments")
        else:
            data=""
            for line in sys.stdin:
                data+=line
            t=asmlTree.asmlTree(data)
            t.registerAllocation_Spill()
            #print(t) #to print AST uncoment this line
            with open(sys.argv[2],'w') as file:
                data=file.write(t.generateAsm())
    elif sys.argv[1]=='-fo':
        if len(sys.argv)<3:
            sys.exit("Insufficient arguments")
        else:
            with open(sys.argv[2],'r') as file:
                data=file.read()
            t=asmlTree.asmlTree(data)
            t.registerAllocation_Spill()
            #print(t) #to print AST uncoment this line
            newFile=os.path.splitext(sys.argv[2])[0]+".s"
            with open(newFile,'w') as file:
                data=file.write(t.generateAsm())   


if __name__ == '__main__':
    sys.exit(main())