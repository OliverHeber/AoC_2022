import heapq


lines = []
newLine = []
with open('input.txt') as file:
    for line in file:
        if line.rstrip() == '':
            lines.append(newLine)
            newLine = []
        else:
            newLine.append(line.rstrip())

mx = []
runSum = 0

for line in lines:
    for v in line:
        runSum += int(v)
    mx.append(runSum)
    runSum = 0
print(sum(heapq.nlargest(3,mx)))
    
