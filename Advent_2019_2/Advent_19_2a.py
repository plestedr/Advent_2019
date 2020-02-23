import os

os.chdir(r'C:\Users\Bob\Documents\GitHub\Advent_2019\Advent_2019_2a')

cycle = 0
pointer = 0
opcodes = []

read_line = open('Input_2a.txt', 'r')
for codes in read_line:
    opcodes = list(map(int,codes.split(',')))

# per instructions, update these by hand before processing
opcodes[1] = 12
opcodes[2] = 2

opcode_len = len(opcodes)

print(f'There are {opcode_len} elements')

# for elem in opcodes:
#    print(f'{elem}')

for cycle in range(0, opcode_len//4):
    pointer = cycle * 4
    next_op = opcodes[pointer]
#    print(f'Cycle is {cycle} Pointer is {pointer}: ', end=' ')
#    print(*opcodes, sep = ", ")
    if next_op == 99:
        print(f'Final value is {opcodes[0]}')
        exit()
    elif next_op == 1:
        opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] + opcodes[opcodes[pointer+2]]
    elif next_op == 2:
        opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] * opcodes[opcodes[pointer+2]]
    else:
        print(f'Invalid operation: {next_op}')
