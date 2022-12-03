def main():
    with open("inputDayThreeQ1.txt") as file_in:
        lines = []
        firstHalf = []
        secondHalf = []
        for line in file_in:
            mid = len(line) // 2
            for i, ch in enumerate(line.rstrip("\n")):
                if i < mid:
                    firstHalf.append(ch)
                else:
                    secondHalf.append(ch)
            lines.append([firstHalf.copy(), secondHalf.copy()])
            firstHalf = []
            secondHalf = []

        same = []
        rucksack = set()
        for l1, l2 in lines:
            for x in l1:
                if x in l2:
                    rucksack.add(x)
            for item in rucksack:
                same.append(str(item))
            rucksack = set()

        # uppercase a = 65
        # lowercase a = 97
        cnt = 0
        for item in same:
            if item.isupper():
                cnt += ord(item) - 38
            elif item.islower():
                cnt += ord(item) - 96
        print(cnt)


if __name__ == "__main__":
    main()
