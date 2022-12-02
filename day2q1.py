def main():
    with open("input3.txt") as file_in:
        lines = []
        for line in file_in:
            # lines.append(int(line.rstrip('\n')))
            lines.append(line.split())
        print(lines)


# ---X--- A for Rock, B for Paper, and C for Scissors.
# ---Y--- X for Rock, Y for Paper, and Z for Scissors.

# 1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

    score = 0
    for x, y in lines:
        match y:
            case 'X':
                score += 1
                score += checkWin(x, y)

            case 'Y':
                score += 2
                score += checkWin(x, y)
            case 'Z':
                score += 3
                score += checkWin(x, y)
    print(score)


def checkWin(x, y):
    if x == 'A' and y == 'X':
        return 3
    if x == 'A' and y == 'Y':
        return 6
    if x == 'A' and y == 'Z':
        return 0

    if x == 'B' and y == 'X':
        return 0
    if x == 'B' and y == 'Y':
        return 3
    if x == 'B' and y == 'Z':
        return 6

    if x == 'C' and y == 'X':
        return 6
    if x == 'C' and y == 'Y':
        return 0
    if x == 'C' and y == 'Z':
        return 3


if __name__ == "__main__":
    main()
