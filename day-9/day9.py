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

# function that will model the rope physics for num_ropes ropes. this function
# returns the number of unique positions visited by the tail of the rope
def model_rope(instructions, num_ropes):
    # define variables
    head_dict = {'U': [0, 1], 'L': [1, 0], 'D': [0, -1], 'R': [-1, 0]}
    tail_pos = set()
    rope_pos = [[0, 0] for i in range(0, num_ropes)]

    # interate through instructions
    for instr in instructions:
        # initialize variables
        instr = instr.split(' ')
        head_update_vals = head_dict[instr[0]]
        x_head, y_head = head_update_vals[0], head_update_vals[1]
        dist = int(instr[1])

        # now update the rope, and add the position of the final rope to the tail_pos set
        for i in range(0, dist):
            # update head
            rope_pos[0][0] += x_head
            rope_pos[0][1] += y_head
            
            # update tail
            for j in range(0, num_ropes-1):
                rope_pos[j+1][0], rope_pos[j+1][1] = update_rope(rope_pos[j][0], rope_pos[j][1], rope_pos[j+1][0], rope_pos[j+1][1])
            tail_pos.add((rope_pos[num_ropes-1][0], rope_pos[num_ropes-1][1]))
    
    # return the number of positions visited by the tail of the rope
    return len(tail_pos)

# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    instructions = f.read().split('\n')

    # perform part 1 and part 2, and print results
    print(model_rope(instructions, 2))
    print(model_rope(instructions, 10))
    
    # close file
    f.close()

if __name__ == '__main__':
    main()