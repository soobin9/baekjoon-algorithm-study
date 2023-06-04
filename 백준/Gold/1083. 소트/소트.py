N = int(input())
numList = list(map(int, input().split()))
S = int(input())

checkIndex = 0
swipe = 0
while (swipe < len(numList)):
    # print(swipe, ':', *numList)
    possibleMax = numList[swipe]
    possibleMaxIndex = swipe
    count = 0
    for i in range(swipe + 1, len(numList)):
        # print(i, ' --', numList[i], ' > ', possibleMax)
        
        # 횟수 넘어갔으면 넘어감 
        if (i - swipe) > S:
            break
        
        if numList[i] > possibleMax:
            possibleMax = numList[i]
            possibleMaxIndex = i
            count = i - swipe

    # 이미 첫번째 인덱스가 가장 크면 while문 종료
    # if possibleMaxIndex == 0:
    #    break
    
    # print(S - count, ' !! ', count)
    # swap할 수 있다면 
    if (S - count) >= 0 and count > 0 :
        # print('check')
        del numList[possibleMaxIndex]
        numList.insert(swipe, possibleMax)
        
        S = S - count
    
    
    swipe += 1 
    
    
# https://yeomss.tistory.com/160
print(*numList)