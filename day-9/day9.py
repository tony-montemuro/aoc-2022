# function that will update the head position
def update_head(x_head, y_head, dir):
    match dir:
        case 'U':
            y_head += 1
        case 'L':
            x_head += 1
        case 'D':
            y_head -= 1
        case 'R':
            x_head -= 1
    return x_head, y_head


def update_rope(x_head, y_head, x_tail, y_tail):
    # first, handle these 4 cases:
    # . H .
    # H T H
    # . H .
    if abs(x_head-x_tail) == 2 and y_head-y_tail == 0:
        x_tail = x_tail-1 if x_head < x_tail else x_tail+1
    elif abs(y_head-y_tail) == 2 and x_head-x_tail == 0:
        y_tail = y_tail-1 if y_head < y_tail else y_tail+1

    # next, handle these twelve cases:
    # H H . H H
    # H . . . H
    # . . T . .
    # H . . . H
    # H H . H H
    elif abs(x_head-x_tail) == 2 or abs(y_head-y_tail) == 2:
        x_tail = x_tail-1 if x_head < x_tail else x_tail+1
        y_tail = y_tail-1 if y_head < y_tail else y_tail+1
    
    # return new tail values
    return x_tail, y_tail

# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    instructions = f.read().split('\n')
    
    # define variables used in part 1
    tail_pos = set()
    x_head, y_head = 0, 0
    x_tail, y_tail = 0, 0

    # iterate through the instructions
    for instr in instructions:
        # get direction and distance from instruction
        instr = instr.split(' ')
        dir = instr[0]
        dist = int(instr[1])

        # now update the rope dist times, and add the position of the tail to the tail_pos set
        for i in range(0, dist):
            x_head, y_head = update_head(x_head, y_head, dir)
            x_tail, y_tail = update_rope(x_head, y_head, x_tail, y_tail)
            tail_pos.add((x_tail, y_tail))

    # print result for part 1
    print(len(tail_pos))

    # define variables used in part 2
    num_ropes = 10
    tail_pos = set()
    rope_pos = [[0, 0] for i in range(0, num_ropes)]
    
    # interate through instructions
    for index, instr in enumerate(instructions):
        # get direction and distance from instruction
        instr = instr.split(' ')
        dir = instr[0]
        dist = int(instr[1])

        # now update the rope dist times, and add the position of the final rope to the tail_pos set
        for i in range(0, dist):
            rope_pos[0][0], rope_pos[0][1] = update_head(rope_pos[0][0], rope_pos[0][1], dir)
            for j in range(0, num_ropes-1):
                rope_pos[j+1][0], rope_pos[j+1][1] = update_rope(rope_pos[j][0], rope_pos[j][1], rope_pos[j+1][0], rope_pos[j+1][1])
            tail_pos.add((rope_pos[9][0], rope_pos[9][1]))

    # print result for part 2
    print(len(tail_pos))
    
    # close file
    f.close()

if __name__ == '__main__':
    main()