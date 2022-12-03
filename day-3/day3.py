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
    mid = int(len(sack)/2)
    set1, set2 = set(sack[0:mid]), set(sack[mid:len(sack)])
    common = list(set1.intersection(set2))[0]
    items.append(common)

# now, based on the priorities dictionary, determine the sum of all common items
sum_1 = sum([priorities[item] for item in items])
print(sum_1)

# iterate through the rucksacks in sets of 3, and determine the common item among
# the three rucksacks
items = []
for i in range(0, len(rucksacks)-1, 3):
    set1, set2, set3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
    common = list(set1.intersection(set2).intersection(set3))[0]
    items.append(common)

# now, based on the priorities dictionary, determine the sum of all common items
sum_2 = sum([priorities[item] for item in items])
print(sum_2)

# close file
f.close()