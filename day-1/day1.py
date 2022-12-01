# open file
f = open("puzzle.txt", "r")
calories = f.read().split('\n')

# loop through list of calories, and find the sum of calories for each elf
elves = []
elf = 0
for c in calories:
    if c == '':
        elves.append(elf)
        elf = 0
    else:
        elf += int(c)
elves.append(elf)

# part 1: find the elf with most number of calories
elves.sort(reverse=True)
print(elves[0])

# part 2: find the 3 elves with the most number of calories, and find sum
print(elves[0]+elves[1]+elves[2])

# close file
f.close()