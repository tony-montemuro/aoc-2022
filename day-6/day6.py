# open file
f = open("puzzle.txt", "r")
data = f.readline()

# find the first start-of-packet
buffer = data[0:3]
pos = 3
found = False
while not found:
    buffer += str(data[pos])
    dupes = set(buffer)
    if len(dupes) == 4:
        found = True
    buffer = buffer[1:]
    pos += 1
print(pos)

# find the first start-of-message
buffer = data[0:13]
pos = 13
found = False
while not found:
    buffer += str(data[pos])
    dupes = set(buffer)
    print(dupes)
    if len(dupes) == 14:
        found = True
    buffer = buffer[1:]
    pos += 1
print(pos)

# close file
f.close()