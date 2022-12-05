# imports
from re import findall
from copy import deepcopy

# function used to print the message from the list of stacks
def print_message(stacks):
    message = ''
    for stack in stacks:
        message += stack.pop()
    print(message)

# open file
f = open("puzzle.txt", "r")
input = f.read().split('\n')

# first, find the index of the blank line. this will separate the input into two parts
num_blank = -1
line = '...'
while not line == '':
    num_blank+=1
    line = input[num_blank]

# next, use the line above the blank line to determine how many crates there are
num_crates = int(input[num_blank-1].replace(' ', '')[-1])

# with this number, we can create a two dimensonal arrays of lists representing each stack of crates
stacks = [[] for i in range(num_crates)]

# now, we can fill up the crates
for i in range(0, num_blank-1):
    for j in range(0, num_crates):
        crate_index = 4*j+1
        crate = input[i][crate_index]
        if (crate != ' '):
            stacks[j].append(crate)

# we actually need to reverse the order of the crates (also a hard copy for part 2)
stacks_1 = [stack[::-1] for stack in stacks]
stacks_2 = deepcopy(stacks_1)

# once we have that, we can begin executing instructions
for i in range(num_blank+1, len(input)):
    instr = findall(r'\d', input[i])
    num_crates, origin, dest = 0, 0, 0
    if len(instr) == 4:
        num_crates, origin, dest = int(instr[0]+instr[1]), int(instr[2])-1, int(instr[3])-1
    else:
        num_crates, origin, dest = int(instr[0]), int(instr[1])-1, int(instr[2])-1

    # part 1
    j = num_crates
    while j > 0:
        crate = stacks_1[origin].pop()
        stacks_1[dest].append(crate)
        j -= 1
    
    # part 2
    crate_arr = []
    j = num_crates
    while j > 0:
        crate = stacks_2[origin].pop()
        crate_arr.append(crate)
        j -= 1
    while len(crate_arr) != 0:
        crate = crate_arr.pop()
        stacks_2[dest].append(crate)

# finally, once we have executed all instructions, we need to pop the top crate off each stack
# to create the message. do this for both set of stacks
print_message(stacks_1)
print_message(stacks_2)

# close file
f.close()