# open file
f = open("puzzle.txt", "r")
grid = f.read().split('\n')

# iterate through grid, and count the number of visible trees
visible = (2 * len(grid) + 2 * len(grid[0])) - 4
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        # initialize variables
        is_visible = False
        tree = int(grid[y][x])

        # first, check for trees to the left
        ctr = 0
        for i in range(0, x):
            if int(grid[y][i]) < tree:
                ctr += 1
        if ctr == x:
            is_visible = True

        # next, check for trees to the top
        if not is_visible:
            ctr = 0
            for i in range(0, y):
                if int(grid[i][x]) < tree:
                    ctr += 1
            if ctr == y:
                is_visible = True

        # next, check for trees to the right
        if not is_visible:
            length = len(grid[y])-1
            ctr = 0
            for i in range(length, x, -1):
                if int(grid[y][i]) < tree:
                    ctr += 1
            if ctr == length-x:
                is_visible = True
        
        # finally, check for trees to the bottom
        if not is_visible:
            length = len(grid)-1
            ctr = 0
            for i in range(length, y, -1):
                if int(grid[i][x]) < tree:
                    ctr += 1
            if ctr == length-y:
                is_visible = True

        # if is_visible is set to true, incrememt visible count
        if is_visible:
            visible += 1
print(visible)

# now, we want to find the highest scenic score possible
highest_score = 0
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        # initialize variables
        left, up, right, down = 1, 1, 1, 1
        tree = int(grid[y][x])

        # first, left trees
        i = x-1
        while i > 0 and int(grid[y][i]) < tree:
            left += 1
            i -= 1

        # next, up trees
        i = y-1
        while i > 0 and int(grid[i][x]) < tree:
            up += 1
            i -= 1

        # next, right trees
        i = x+1
        while i < len(grid[y])-1 and int(grid[y][i]) < tree:
            right += 1
            i += 1

        # finally, down trees
        i = y+1
        while i < len(grid)-1 and int(grid[i][x]) < tree:
            down += 1
            i += 1

        # update highest_score if this scenic score was larger
        scenic_score = left*up*right*down
        if scenic_score > highest_score:
            highest_score = scenic_score
print(highest_score)
 
# close file
f.close()