# open file
f = open("puzzle.txt", "r")
sections = f.read().split('\n')

# go through each pair of sections, and count each time there is total overlap or partial overlap
t1, t2 = 0, 0
for section in sections:
    assignments = section.split(',')
    first, second = assignments[0].split('-'), assignments[1].split('-')
    l1, u1 = int(first[0]), int(first[1])
    l2, u2 = int(second[0]), int(second[1])
    if l2 >= l1 and u1 >= u2 or l1 >= l2 and u2 >= u1:
        t1 += 1
    if l1 >= l2 and l1 <= u2 or l2 >= l1 and l2 <= u1:
        t2 += 1
print(t1, t2)

# close file
f.close()