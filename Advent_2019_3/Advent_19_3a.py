import os

os.chdir(r'C:\Users\agar2\Documents\github\Advent_2019\Advent_2019_3')

Input_File = 'dist_135.txt'


opcodes = []

def generate_result(op_c):
    op_c_len = len(op_c)
#    print(f'Opcodes {op_c_len}')
    cycle = 0
    pointer = 0

    for cycle in range(0, op_c_len//4):
        pointer = cycle * 4
        next_op = op_c[pointer]
#    print(f'Cycle is {cycle} Pointer is {pointer}: ', end=' ')
#    print(*op_c, sep = ", ")
        if next_op == 99:
            return op_c[0]
        elif next_op == 1:
            op_c[op_c[pointer+3]] = op_c[op_c[pointer+1]] + op_c[op_c[pointer+2]]
        elif next_op == 2:
            op_c[op_c[pointer+3]] = op_c[op_c[pointer+1]] * op_c[op_c[pointer+2]]
        else:
            print(f'Invalid operation: {next_op}')
            print(*op_c, sep = ", ")
            print(f'Cycle: {cycle}')
            print(f'Noun: {noun}   Verb: {verb}')
            exit()

for noun in list(range(99)):
    for verb in list(range(99)):
        read_line = open(Input_File.txt, 'r')
        for codes in read_line:
            opcodes = list(map(int,codes.split(',')))

        opcodes[1] = noun
        opcodes[2] = verb
        print(*opcodes, sep = ", ")

        if generate_result(opcodes) == 19690720:
            print(f'Noun is {noun} and verb is {verb}')
            print(100 * noun + verb)
            exit()
