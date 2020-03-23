#Kieran Thompson
#Day 2/2019 - 1202 Program Alarm

def getValueAt(program, no):
    return int(program[no])

##function to do the computation of the machine
def intCode1():
    ##TESTS
    ##program = [1,0,0,0,99]
    ##program = [1,1,1,4,99,5,6,0,99]

    file = open("input.txt","r")
    program = file.read().split(",")
    program = [ int(x) for x in program]
    file.close()

    ##setup the basic instruction elements 
    opcodeList = [1,2,99]
    instructionSize = 4 

    ##loop through program
    for pc in range(0, len(program), instructionSize):

        ##get the opcode of the instruction
        opcode = getValueAt(program, pc)

        ##or exit if the opcode is 99
        if (opcode == 99):
            return program
        else:

            ##get the operands 
            operand1 = getValueAt(program, int(pc+1) )
            operand2 = getValueAt(program, int(pc+2) )
            result = getValueAt(program, int(pc+3) )

            ##print values of instructions 
            print("opcode: " + str(opcode))

            ##do the instructions with the set opcodes
            ##add
            if (opcode == 1):
                print("ADD")
                program[result] = program[operand1] + program[operand2] 
               
            ##mul
            elif (opcode == 2):
                print("MUL")
                program[result] = program[operand1] * program[operand2]

            
print(intCode1())
