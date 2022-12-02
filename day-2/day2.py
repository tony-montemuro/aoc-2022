# open file
f = open("puzzle.txt", "r")
guide = f.read().split('\n')

# part 1
# A = ROCK, B = PAPER, C = SCISSORS
# X = ROCK, Y = PAPER, C = SCISSORS
score = 0
for round in guide:
    letters = round.split(' ')
    elf, human = letters[0], letters[1]
    match elf:
        case 'A':
            match human:
                case 'X':
                    score += 1 + 3
                case 'Y':
                    score += 2 + 6
                case 'Z':
                    score += 3 + 0
        case 'B':
            match human:
                case 'X':
                    score += 1 + 0
                case 'Y':
                    score += 2 + 3
                case 'Z':
                    score += 3 + 6
        case 'C':
            match human:
                case 'X':
                    score += 1 + 6
                case 'Y':
                    score += 2 + 0
                case 'Z':
                    score += 3 + 3
print(score)

# part 2
score = 0
# A = ROCK, B = PAPER, C = SCISSORS
# X = LOSE, B = DRAW, C = WIN
for round in guide:
    letters = round.split(' ')
    elf, human = letters[0], letters[1]
    match elf:
        case 'A':
            match human:
                case 'X':
                    score += 3 + 0
                case 'Y':
                    score += 1 + 3
                case 'Z':
                    score += 2 + 6
        case 'B':
            match human:
                case 'X':
                    score += 1 + 0
                case 'Y':
                    score += 2 + 3
                case 'Z':
                    score += 3 + 6
        case 'C':
            match human:
                case 'X':
                    score += 2 + 0
                case 'Y':
                    score += 3 + 3
                case 'Z':
                    score += 1 + 6
print(score)

# close file
f.close()