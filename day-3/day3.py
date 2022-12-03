# open file
f = open("puzzle.txt", "r")
rucksacks = f.read().split('\n')

# define dictionary for letter values
priorities = {}
for i in range(1, 27):
    priorities[chr(i+96)] = i
for i in range(1, 27):
    priorities[chr((i)+64)] = i+26

# iterate through each rucksack, split each into compartments, and determine
# the common item among both compartments
items = []
for sack in rucksacks:
    set1, set2 = set(), set()
    mid = int(len(sack)/2)
    c1, c2 = sack[0:mid], sack[mid:len(sack)]
    for c in c1:
        set1.add(c)
    for c in c2:
        set2.add(c)
    for e1 in set1:
        for e2 in set2:
            if e1 == e2:
                items.append(e1)

# now, based on the priorities dictionary, determine the sum of all common items
sum_1 = sum([priorities[item] for item in items])
print(sum_1)

# iterate through the rucksacks in sets of 3, and determine the common item among
# the three rucksacks
items = []
for i in range(0, len(rucksacks)-1, 3):
    set1, set2, set3 = set(), set(), set()
    s1, s2, s3 = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
    for c in s1:
        set1.add(c)
    for c in s2:
        set2.add(c)
    for c in s3:
        set3.add(c)
    for e1 in set1:
        for e2 in set2:
            for e3 in set3:
                if e1 == e2 and e2 == e3:
                    items.append(e1)

# now, based on the priorities dictionary, determine the sum of all common items
sum_2 = sum([priorities[item] for item in items])
print(sum_2)

# close file
f.close()