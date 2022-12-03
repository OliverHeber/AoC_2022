def main():
    with open("inputDayTwoQ2.txt") as file_in:
        lines = []
        for line in file_in:
            # lines.append(int(line.rstrip('\n')))
            lines.append(line.split())
        print(lines)


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    score = 0
    for x, y in lines:
        match y:
            case 'X':
                score += 0
                score += getLosingMove(x)
            case 'Y':
                score += 3
                score += getDrawingMove(x)
            case 'Z':
                score += 6
                score += getWinningMove(x)
    print(score)


# ---X--- A for Rock, B for Paper, and C for Scissors.
# ---Y--- X for Rock, Y for Paper, and Z for Scissors.

# 1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
def getWinningMove(x):
    if x == 'A':
        return 2
    if x == 'B':
        return 3
    if x == 'C':
        return 1

def getDrawingMove(x):
    if x == 'A':
        return 1
    if x == 'B':
        return 2
    if x == 'C':
        return 3

def getLosingMove(x):
    if x == 'A':
        return 3
    if x == 'B':
        return 1
    if x == 'C':
        return 2


if __name__ == "__main__":
    main()
