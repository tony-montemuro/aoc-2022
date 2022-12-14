# imports
from sys import maxsize
from math import floor

# transform x for part 1
def t_x_1(x, x_min, padding):
    return x-x_min+floor(padding/2)

# transform x for part 2
def t_x_2(x, x_max, x_min, x_scale):
    return (x-x_min+1)+(floor(x_scale/2)*(x_max-x_min+1))

# function that will simulate sand being dropped
def drop_sand(part, cave, sand_origin):
    # now, let's drop sand until we can no longer do so
    sand_ctr = 0
    droppable = True
    while (droppable):
        x, y = sand_origin[0], sand_origin[1]
        landed = False
        while(not landed):
            if y == len(cave)-1:
                landed = True
            elif cave[y+1][x] == '.':
                y += 1
            elif cave[y+1][x-1] == '.':
                y += 1
                x -= 1
            elif cave[y+1][x+1] == '.':
                y += 1
                x += 1
            else:
                landed = True
        if part == 1 and y == len(cave)-1:
            droppable = False
        else:
            cave[y][x] = 'o'
            sand_ctr += 1
            if part == 2 and x == sand_origin[0] and y == sand_origin[1]:
                droppable = False
    return sand_ctr


# main function
def main():
    # open file and parse
    f = open("puzzle.txt", "r")
    rock_paths, coordinates = f.read().split('\n'), []

    # now, let's find the min and max x, as well as max y
    min_x, max_x = maxsize, -maxsize-1
    max_y = -maxsize-1
    for path in rock_paths:
        l = []
        for p in path.split('->'):
            pair = eval(p.strip())
            if pair[0] < min_x:
                min_x = pair[0]
            if pair[0] > max_x:
                max_x = pair[0]
            if pair[1] > max_y:
                max_y = pair[1]
            l.append(pair)
        coordinates.append(l)
    
    # now, we can generate our cave based on this knowledge
    padding_x, padding_y = 3, 2
    sand_origin = (t_x_1(500, min_x, padding_x), 0)
    cave = [['.' for i in range(0, max_x-min_x+padding_x)] for j in range(0, max_y+padding_y)]
    for coord in coordinates:
        for i in range(0, len(coord)-1):
            p1, p2 = coord[i], coord[i+1]
            if p1[0] != p2[0]:
                lower, upper = min(p1[0], p2[0]), max(p1[0], p2[0])
                for j in range(lower, upper+1):
                    cave[p1[1]][t_x_1(j, min_x, padding_x)] = '#'
            else:
                lower, upper = min(p1[1], p2[1]), max(p1[1], p2[1])
                for j in range(lower, upper):
                    cave[j][t_x_1(p1[0], min_x, padding_x)] = '#'
    cave[sand_origin[1]][sand_origin[0]] = '+'

    # part 1 answer
    print(drop_sand(1, cave, sand_origin))

    # in part 2, the entire bottom floor is covered in rock
    x_scale = 9
    sand_origin = (t_x_2(500, max_x, min_x, x_scale), 0)
    cave = [['.' for i in range(0, (max_x-min_x+1)*x_scale)] for j in range(0, max_y+padding_y)]
    cave.append(['#' for i in range(0, (max_x-min_x)*x_scale)])
    for coord in coordinates:
        for i in range(0, len(coord)-1):
            p1, p2 = coord[i], coord[i+1]
            if p1[0] != p2[0]:
                lower, upper = min(p1[0], p2[0]), max(p1[0], p2[0])
                for j in range(lower, upper+1):
                    cave[p1[1]][t_x_2(j, max_x, min_x, x_scale)] = '#'
            else:
                lower, upper = min(p1[1], p2[1]), max(p1[1], p2[1])
                for j in range(lower, upper):
                    cave[j][t_x_2(p1[0], max_x, min_x, x_scale)] = '#'
    cave[sand_origin[1]][sand_origin[0]] = '+'

    # part 2
    print(drop_sand(2, cave, sand_origin))

    # close file
    f.close()

if __name__ == "__main__":
    main()