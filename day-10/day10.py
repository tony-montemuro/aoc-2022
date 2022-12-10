# return the index for horizontal position of the screen
def get_index(time, screen_line):
    return time-(40*screen_line)-1

# function that checks for special cycles, and updates information accordingly
def cycle(time, register_vals, register, screen_line, screen):
    # special case: 20th, 60th, 100thm 140th, or 180th cycle. we want to take
    # the product of the register value and time, and append to register_vals list
    if (time-20) % 40 == 0:
        register_vals.append(time*register)

    # special case 2: 40th, 80th, 120th, 160th, 200th, or 240th cycle. we want to shift
    # down to the next line of the screen. do so by adding 1 to screen_line
    if (time-1) % 40 == 0 and (time-1) > 0:
        screen_line += 1

    # calculate horizontal index along screen based on the time and screen_line. if this value is
    # within the sprite bounds, print a # at this location. otherwise, keep it a dot
    hor_index = get_index(time, screen_line)
    if hor_index >= register-1 and hor_index <= register+1:
        screen[screen_line][hor_index] = '#'

    # return any updated values
    return register_vals, screen_line, screen

def main():
    # open file
    f = open("puzzle.txt", "r")
    instructions = f.read().split('\n')
    addr_time = 2

    # initialize variables used in part 1
    register, time = 1, 1
    register_vals = []

    # initalize variables used in part 2
    screen = [['.' for i in range(0, 40)] for j in range(0, 6)]
    screen_line = 0

    # go through each instruction
    for i in instructions:
        # parse instruction
        i_arr = i.split(' ')
        instr = i_arr[0]

        # case 1: addx instruction
        if instr == 'addx':
            val = int(i_arr[1])
            for j in range(0, addr_time):
                register_vals, screen_line, screen = cycle(time, register_vals, register, screen_line, screen)
                time += 1
            # update register
            register += val

        # case 2: noop instruction
        else:
            register_vals, screen_line, screen = cycle(time, register_vals, register, screen_line, screen)
            time += 1
    
    # print results of part 1
    print(sum(register_vals))

    # print results for part 2
    [print(line) for line in screen]

    # close file
    f.close()

if __name__ == '__main__':
    main()