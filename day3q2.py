def main():
    with open("inputDayThreeQ1.txt") as file_in:
        lines = []
        group = []
        newGroup = 0
        for line in file_in:
            if newGroup == 3:
                lines.append(group.copy())
                group = []
                newGroup = 0  
            group.append(line.rstrip("\n"))
            newGroup += 1
        lines.append(group.copy())
        # print(lines)
            
        # lines = [['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg'],['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']]

        same = []
        badge = set()
        for l1, l2, l3 in lines:
            for x in l1:
                if x in l2 and x in l3:
                    badge.add(x)
            for b in badge:
                same.append(str(b))
            badge = set()
        # print(same)

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
