
##### input 시작 ##### 
# N극은 0, S극은 1, 12시부터 시계 방향으로 나타남 
wheels = [] 
for i in range(4):
    wheels.append(list(map(int,input())))

# 회전 횟수 K 
K = int(input())

# 회전시킨 톱니바퀴의 번호, 방향 (1 시계방향, -1 반시계방향)
rotated = [] 
for i in range(K):
    temp = list(map(int, input().split())) # 번호, 방향 
    mark = []
    if temp[1] == 1:
        mark = [temp[0] - 1, True] # 1,2,3,4 번으로 들어오기 때문에 보정 
    else: 
        mark = [temp[0] - 1, False]
    
    # 번호, 방향 
    rotated.append(mark)
##### input 종료 ##### 

# 시계방향, 반시계방향 
def move(wheel, isClockWise):
    if isClockWise == True:
        # print(wheel, isClockWise)
        wheel = [wheel[7], wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5], wheel[6]]
    elif isClockWise == False:
        # print(isClockWise, debug(wheel))
        wheel = [wheel[1], wheel[2], wheel[3], wheel[4], wheel[5], wheel[6], wheel[7], wheel[0]]
        # print(isClockWise, debug(wheel))
    return wheel 

# 톱니바퀴 회전 
def rotate(start, isClockWise, isUp, directions):
    directions[start] = isClockWise
    
    if isUp == False :
        if (start - 1) >= 0 :
            if (wheels[start -1][2] == wheels[start][6]):
                directions[start -1] = None 
            else:
                directions[start - 1] = not directions[start]
      
                # 반례 - 재귀 통해서 확인해야 함 ,, 
                rotate(start -1, directions[start -1], isUp, directions)
                
    if isUp == True : 
        if (start + 1) <= 3 :
            if (wheels[start +1][6] == wheels[start][2]):
                directions[start + 1] = None 
            else:
                directions[start + 1] = not directions[start]
                
                # 반례 - 재귀 통해서 확인해야 함 ,, 
                rotate(start + 1, directions[start + 1], isUp, directions)
    
    return directions

# N,S 형태로 표현 
def debug(wheel):
    result = '' 
    for i in wheel:
        if i == 0:
            result = result + 'N'
        else:
            result = result + 'S'
    return result

# main 
# print(debug(wheels[0]), debug(wheels[1]), debug(wheels[2]), debug(wheels[3]))
for i in range(K):
    # 방향 판단 
    # print(-1)
    directions = [None,None,None,None]
    directions = rotate(rotated[i][0], rotated[i][1],False, directions)
    directions = rotate(rotated[i][0], rotated[i][1],True, directions)
    # print(i, directions)
    for j in range(4):
        wheels[j] = move(wheels[j], directions[j])
        
    # print(i, debug(wheels[0]), debug(wheels[1]), debug(wheels[2]), debug(wheels[3]))
        


# print(debug(move(one, False)))

### 답 
print(wheels[0][0]*1 + wheels[1][0]*2 + wheels[2][0]*4 + wheels[3][0]*8)
    

    

