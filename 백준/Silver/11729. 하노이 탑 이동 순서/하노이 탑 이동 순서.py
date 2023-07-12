n = int(input())

count = 0
startList = []
destList = []
def hanoi(n, start, dest, sub):
    global count
    
    if n == 1:
        count += 1
        startList.append(start)
        destList.append(dest)
        return
    
    hanoi(n - 1, start, sub, dest)
    count += 1
    startList.append(start)
    destList.append(dest)
    hanoi(n - 1, sub, dest, start)

hanoi(n, 1, 3, 2)

print(count)
for i in range(count):
    print(startList[i], destList[i])
