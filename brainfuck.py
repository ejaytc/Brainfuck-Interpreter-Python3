#!/usr/bin/env python3
#brainfuck.py - Brainfuck-Interpreter
#Hello World! = ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]"
#Nested loop = "+++[>+++<[-]]"

memory = [0]*30000
stock = []
ptIndex = 0
output = ''

def brainf_program(sCode):
    
    global memory, stock, ptIndex, output
    loop = 0
    
    while loop < len(sCode):
        if sCode[loop] == '>':
            ptIndex += 1
        elif sCode[loop] == '<':
            ptIndex -= 1
        elif sCode[loop] == '+':
            memory[ptIndex] += 1
        elif sCode[loop] == '-':

            if memory[ptIndex] != 0:
                memory[ptIndex] -= 1
            else: memory[ptIndex] = 0

        elif sCode[loop] ==',':
            getchar = input()
            memory[ptIndex] += ord(getchar)
        elif sCode[loop] == '.':
             output += chr(memory[ptIndex])
        elif sCode[loop] == '[':
            if loop  not in stock:
                stock.append(loop)
        elif sCode[loop] == ']':
            if memory[ptIndex] != 0:
                loop = stock[-1] -1
            else:
                stock.pop()
        loop += 1
if __name__ == "__main__":
    print("="*50)
    print("{} BrainFuck Interpreter".format(" "*12))
    print("="*50)
    while True:
        sCode = input("~")
        brainf_program(sCode)
        print(output, end = '\n')