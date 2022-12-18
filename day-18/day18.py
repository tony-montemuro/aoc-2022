# adjacency function
def is_adjacent(c1, c2):
    if (c1[0] == c2[0]+1 or c1[0] == c2[0]-1) and (c1[1] == c2[1]) and (c1[2] == c2[2]):
        return True
    if (c1[1] == c2[1]+1 or c1[1] == c2[1]-1) and (c1[0] == c2[0]) and (c1[2] == c2[2]):
        return True
    if (c1[2] == c2[2]+1 or c1[2] == c2[2]-1) and (c1[1] == c2[1]) and (c1[0] == c2[0]):
        return True
    return False

# function that will return number of sides
def get_num_sides(cubes):
    # set up dictionary for the cubes. key = cube, value = adjacent number of adjacent cubes
    cubes_dict = {}
    for cube in cubes:
        cubes_dict[cube] = 0

    # now, loop through the cubes, and determine adjacent cubes for each cube
    for primary in cubes:
        for secondary in cubes:
            if is_adjacent(primary, secondary):
                cubes_dict[primary] += 1
    
    # calculate number of sides
    num_sides = 0
    for num_adjacent in cubes_dict.values():
        num_sides += 6-num_adjacent

    # return number of sides
    return num_sides, cubes_dict

# is pocket function: will return a list of air blocks if it's a true pocket. otherwise, it will return
# an empty list
def is_pocket(visited, x, y, z, cubes_dict, x_range, y_range, z_range):
    # init variables
    min_x, min_y, min_z = x_range[0], y_range[0], z_range[0]
    max_x, max_y, max_z = x_range[1], y_range[1], z_range[1]
    visited.append((x, y, z))

    # base case: we found an exit!
    if x < min_x or y < min_y or z < min_z or x > max_x or y > max_y or z > max_z:
        return []

    # general case: explore all surrounding blocks if they are not lava cubes
    if (x+1, y, z) not in cubes_dict and (x+1, y, z) not in visited:
        visited = is_pocket(visited, x+1, y, z, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    if (x-1, y, z) not in cubes_dict and (x-1, y, z) not in visited:
        visited = is_pocket(visited, x-1, y, z, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    if (x, y+1, z) not in cubes_dict and (x, y+1, z) not in visited:
        visited = is_pocket(visited, x, y+1, z, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    if (x, y-1, z) not in cubes_dict and (x, y-1, z) not in visited:
        visited = is_pocket(visited, x, y-1, z, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    if (x, y, z+1) not in cubes_dict and (x, y, z+1) not in visited:
        visited = is_pocket(visited, x, y, z+1, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    if (x, y, z-1) not in cubes_dict and (x, y, z-1) not in visited:
        visited = is_pocket(visited, x, y, z-1, cubes_dict, x_range, y_range, z_range)
        if len(visited) == 0:
            return visited
    return visited


# main function
def main():
    # open file
    f = open("puzzle.txt", "r")
    input = f.read().split('\n')
    cubes = [eval(i) for i in input]

    # part 1 answer
    exterior, cubes_dict = get_num_sides(cubes)
    print(exterior)

    # for part 2, we need to find air pockets
    min_x, min_y, min_z = 100000, 100000, 100000
    max_x, max_y, max_z = -1, -1, -1
    for cube in cubes:
        x, y, z = cube[0], cube[1], cube[2]
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
        if z > max_z:
            max_z = z
        if z < min_z:
            min_z = z
    
    # now, we want to get the list of all air pockets.
    pockets = []
    x_range, y_range, z_range = (min_x, max_x), (min_y, max_y), (min_z, max_z)
    for x in range(min_x+1, max_x):
        for y in range(min_y+1, max_y):
            for z in range(min_z+1, max_z):
                cube = (x, y, z)
                if (cube not in cubes_dict and cube not in pockets):
                    pockets.extend(is_pocket([], x, y, z, cubes_dict, x_range, y_range, z_range))

    # part 2 answer
    interior, _ = get_num_sides(pockets)
    print(exterior-interior)

    # close file
    f.close()

if __name__ == "__main__":
    main()