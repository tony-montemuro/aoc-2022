# improts
from functools import cmp_to_key

# RETURNS: -1: l1 < l2 (order is correct for part 2), 1: l1 > l2 (order is incorrect for part 2)
# 0: l1 = l2. useful for part 2
def compare_lists(l1, l2):
    # next, general comparisons: these can be integers and integers,
    # lists and lists, or mixed types
    i = 0
    while i < len(l1) and i < len(l2):
        if type(l1[i]) == int and type(l2[i]) == int:
            if l1[i] > l2[i]:
                return 1
            if l1[i] < l2[i]:
                return -1
        else:
            new_l1, new_l2 = None, None
            if type(l1[i]) == int:
                new_l1 = [l1[i]]
            elif type(l1[i]) == list:
                new_l1 = l1[i]
            if type(l2[i]) == int:
                new_l2 = [l2[i]]
            elif type(l2[i]) == list:
                new_l2 = l2[i]
            result = compare_lists(new_l1, new_l2)
            if result != 0:
                return result
        i += 1

    # if we made it this far, we return based on the length of each list
    if i < len(l1):
        return 1
    if i < len(l2):
        return -1
    return 0

def main():
    # open file
    f = open("puzzle.txt", "r")
    pairs = [pair.split('\n') for pair in f.read().split('\n\n')]

    # iterate through pairs
    ordered_indicies = []
    for index, pair in enumerate(pairs):
        p1, p2 = eval(pair[0]), eval(pair[1])
        if compare_lists(p1, p2) < 0:
            ordered_indicies.append(index+1)
        
    # print answer
    print(sum(ordered_indicies))

    # for part 2, we need to break apart pairs, add the two divider packets, and sort them
    d1, d2 = [[2]], [[6]]
    packets = [d1, d2]
    for p in pairs:
        packets.append(eval(p[1]))
        packets.append(eval(p[0]))
    packets = sorted(packets, key=cmp_to_key(compare_lists))

    # the answer is the product of the indicides of the two divider packets. let's fine them and
    # print result
    for index, p in enumerate(packets):
        if p == d1:
            i1 = index+1
        if p == d2:
            i2 = index+1
    print(i1*i2)

    # close file
    f.close()

if __name__ == "__main__":
    main()