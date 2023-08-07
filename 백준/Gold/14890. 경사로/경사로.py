

# 첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다.
# L : 경사로 길이 
N, L = map(int, input().split())
arr = [[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j,v in enumerate(input().split()):
        arr[i][j] = int(v)

def check(subArr):
    # print(subArr)
    bridge = [False for _ in range(len(subArr))] # 경사로 

    cur = 1
    result = True
    tempArr = subArr.copy()
    
    cnt = 0 
    while (cur < N):
        if result == False: 
            break
        
        prev = tempArr[cur - 1]
        # 차이가 1 나면 경사로 추가함 
        if tempArr[cur] == prev:
            # print('c0', cnt, cur, subArr)
            cur = cur + 1
        elif tempArr[cur] == (prev - 1):
            # print('c1', cnt, cur, tempArr)
            # print(cur + L - 1)
            for i in range(L):
                # print('c1.s', bridge)
                if (cur + i) >= N or bridge[cur + i] == True or (cur + L -1)>=N:
                    #print('why not')
                    result = False
                    break
                if  tempArr[cur + i] != tempArr[cur]:
                    result = False
                    break
                
                bridge[cur + i] = True 
                
            cur = cur + L # cur 자리부터 다시 체크 
            # print('c1.r', cnt, cur, tempArr)
        elif tempArr[cur] == (prev + 1):
            # print('c2', cnt, cur, tempArr, L)
            for i in range(L):
                #print(cur - 1 - i)
                if (cur - 1 - i) < 0 or bridge[cur - 1 - i] == True:
                    result = False
                    break
                if tempArr[cur - 1 - i] != tempArr[cur - 1]:
                    result = False
                    break
                
            cur = cur + 1
            #print('c2.r', cnt, cur, tempArr)
        else:
            # print('c3', cnt, cur, subArr)
            result = False
            break
        
        
    return result
            
        
    

# 시작부터, 아님 뒤에서부터 
debug = 0 
cnt = 0 
for i in range(N):
    tempRow = []
    tempCol = []
    
    for j in range(N):
        tempRow.append(arr[i][j])
        tempCol.append(arr[j][i])
        
    # 경사로 확인
    if (check(tempRow) or check(tempRow[::-1])):
        # print('1', tempRow)
        cnt = cnt + 1
    if (check(tempCol) or check(tempCol[::-1])):
        # print('2', tempCol)
        cnt = cnt + 1
    
    # debug = debug + 1 
    # if debug == 2:
    #     break

print(cnt)
# print(check([2,2,3,3,2,2]))
# print(check([2,2,3,3,2,2]))
# # print(check([3,2,1,1,2,3]))
# print(check([3,2,1,1,2,3]))
# check([3,2,2,1,1,1])
#check([3, 3, 2, 1, 1, 1])
# check([3,3,3,3,3,2])
# check([3,3,3,3,3,2])
# check([3,3,3,3,3,2])
# print(cnt)




