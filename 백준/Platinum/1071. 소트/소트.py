N = int(input())
numList = list(map(int,input().split()))

# 오름차순으로 정렬
numList.sort()

for i in range(len(numList) - 1):
    # print(numList[i], ' :: ', numList)
    if (i > 0 and numList[i] == numList[i - 1]):
        count = count +1
    else:
        count = 0
    
    if (numList[i] + 1) == numList[i + 1]:
        # i + 1 이 최솟값이라면 
        if (numList[-1] == numList[i + 1]):
            temp = numList[-1]
            del numList[-1]
            numList.insert(i - count, temp)
            # print('>', numList)
        else:
            # i + 1 다음으로 최솟값을 찾아서 다음 값으로 넣어줌 
            for nextIndex in range(i +2, len(numList)):
                if numList[nextIndex] > numList[i + 1]:
                    temp = numList[nextIndex]
                    del numList[nextIndex]
                    numList.insert(i + 1, temp)
                    break
                
        
print(*numList)

