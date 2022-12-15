# imports
from math import floor
import time

# function that will return the number of positions in target row that cannont contain beacon
def num_pos(ys, yt, m):
    return (2*m+1)-(2*abs(ys-yt))

def main():
    # open file and parse
    start = time.time()
    f = open("puzzle.txt", "r")
    directions = f.read().split('\n')
    target_y = 2000000
    target_y_positions = set()
    sensor_beacons = []

    # now, let's figure out how many positions cannot be a beacon at target y
    for dir in directions:
        dir = [d.strip() for d in dir.split('=')]
        xs, ys = int(dir[1][:-3]), int(dir[2].split(':')[0])
        xb, yb = int(dir[3][:-3]), int(dir[4])
        manhattan = abs(xs-xb) + abs(ys-yb)
        if abs(target_y-ys) <= manhattan:
            n = num_pos(ys, target_y, manhattan)
            [target_y_positions.add(i) for i in range(xs-floor(n/2), xs+floor(n/2))]
        sensor_beacons.append([(xs, ys), (xb, yb)])

    # answer for part 1
    print(len(target_y_positions))
    print("--- Part 1 took %s seconds ---" % (time.time() - start))

    # for part 2, we must find the single position where a beacon could be to
    # compute the tuning frequency
    start = time.time()
    target = 4000000
    ranges = {}
    for i in range(0, target+1):
        ranges[i] = []
    for s_b in sensor_beacons:
        xs, ys = s_b[0][0], s_b[0][1]
        xb, yb = s_b[1][0], s_b[1][1]
        manhattan = abs(xs-xb) + abs(ys-yb)
        lower = ys-manhattan if ys-manhattan >= 0 else 0
        upper = ys+manhattan+1 if ys+manhattan <= target else target+1
        for y in range(lower, upper):
            n = num_pos(ys, y, manhattan)
            ranges[y].append((xs-floor(n/2) if xs-floor(n/2) >= 0 else 0, xs+floor(n/2) if xs+floor(n/2) <= target else target))

    # now, let's find the special position
    x, y = None, 0
    found = False
    while not found:
        y_range = sorted(ranges[y], key=lambda tup: tup[0])
        i = 0
        while i < len(y_range)-1:
            j = i+1
            while j < len(y_range) and y_range[j][0] <= y_range[i][1] and y_range[j][1] <= y_range[i][1]:
                j += 1
            if j < len(y_range) and y_range[j][0] > y_range[i][1]:
                x = y_range[i][1]+1
                found = True
            i = j
        y += 1
    y -= 1

    # now that we have x and y, let's print the tuning frequency
    print(x*target+y)
    print("--- Part 2 took %s seconds ---" % (time.time() - start))

    # close file
    f.close()

if __name__ == "__main__":
    main()