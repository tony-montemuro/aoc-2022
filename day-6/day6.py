# find the first occurence of marker with length defined by length parameter
def marker_finder(length):
    buffer = data[0:length-1]
    pos = length-1
    found = False
    while not found:
        buffer += str(data[pos])
        dupes = set(buffer)
        if len(dupes) == length:
            found = True
        buffer = buffer[1:]
        pos += 1
    return pos

# open file
f = open("puzzle.txt", "r")
data = f.readline()

# print the first occurence of a marker of different lengths
print(marker_finder(4))
print(marker_finder(14))

# close file
f.close()