# imports
from math import floor

# returns rock based on index i
def get_rock(i):
    rocks = [
        ['#','#','#','#'],
        [
            ['.','#','.'],
            ['#','#','#'],
            ['.','#','.']
        ],
        [
            ['.', '.', '#'],
            ['.', '.', '#'],
            ['#', '#', '#']
        ],
        [
            ['#'],
            ['#'],
            ['#'],
            ['#']
        ],
        [
            ['#','#'],
            ['#','#']
        ]
    ]
    return rocks[i%5]

# make the rock move specified by direction
def push_rock(rock_coordinates, grid, dir):
    shift = -1 if dir == '>' else 1
    for coors in rock_coordinates:
        x, y = coors[0], coors[1]
        if (shift == -1 and coors[0] == 0) or (shift == 1 and coors[0] == len(grid[0])-1) or (grid[y][x+shift] == '#' and [x+shift, y] not in rock_coordinates):
            return
    for i, coords in enumerate(rock_coordinates):
        x, y = coords[0], coords[1]
        grid[y][x] = '.'
        rock_coordinates[i][0] += shift
    for coords in rock_coordinates:
        x, y = coords[0], coords[1]
        grid[y][x] = '#'
    return

# make the rock fall. if rock cannot fall, return True. otherwise, return false.
def fall_rock(rock_coordinates, grid):
    for coors in rock_coordinates:
        x, y = coors[0], coors[1]
        if coors[1] == 0 or (grid[y-1][x] == '#' and [x, y-1] not in rock_coordinates):
            return True
    for i, coords in enumerate(rock_coordinates):
        x, y = coords[0], coords[1]
        grid[y][x] = '.'
        rock_coordinates[i][1] -= 1
    for coords in rock_coordinates:
        x, y = coords[0], coords[1]
        grid[y][x] = '#'
    return False

# get the highest rock in the room
def get_top(top, grid):
    found_very_top = False
    while not found_very_top:
        found_very_top = True
        row = grid[top]
        for c in row:
            if c == '#':
                found_very_top = False
        top += 1
    return top-1

# drop rocks function (returns height of tower)
def manual_drop(n, grid, jet_pattern):
    # drop n rocks
    top, jet_ctr = 0, 0
    for i in range(n):
        # get rock
        rock = get_rock(i)

        # add rock to grid
        rock_coordinates = []
        if type(rock[0]) == list:
            for list_index, l in enumerate(rock):
                for rock_index, r in enumerate(l):
                    y, x = top+3+len(rock)-list_index-1, 4-rock_index
                    grid[y][x] = r
                    if r == '#':
                        rock_coordinates.append([x, y])
        else:
            for rock_index, r in enumerate(rock):
                y, x = top+3, 4-rock_index
                grid[y][x] = r
                if r == '#':
                    rock_coordinates.append([x, y])

        # make rocks fall and move according to jet stream
        rested = False
        while not rested:
            push_rock(rock_coordinates, grid, jet_pattern[jet_ctr])
            jet_ctr = (jet_ctr+1)%len(jet_pattern)
            rested = fall_rock(rock_coordinates, grid)
            # if rested and jet_ctr==2:
            #     print(i+1, get_top(top, grid))

        # update top
        top = get_top(top, grid)

    return get_top(top, grid)

# since this a cylce-based problem, given any n > 1707, we can return the
# height of the tower with only a single manual tower calculation
# NOTE: Many of these numbers seem like magic. I found them by experimenting with manual drop
# function
def auto_drop(n, grid, jet_pattern):
    diff = n-1707
    return (floor(diff/1700)*2642)+(manual_drop(1707+(diff%1700), grid, jet_pattern))

# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    jet_pattern = f.read()

    # answer to part 1
    grid = [['.' for i in range(7)] for j in range(5000)]
    n = 2022
    print(manual_drop(n, grid, jet_pattern))

    # answer to part 2
    grid = [['.' for i in range(7)] for j in range(5000)]
    n = 1000000000000
    print(auto_drop(n, grid, jet_pattern))
   
    # close file
    f.close()

if __name__ == "__main__":
    main()