

dice = [0,0,0,0,0,0]
N, M, x, y, K = list(map(int, input().split()))
maps= []
for _ in range(N):
    maps.append(list(map(int, input().split())))
commands = list(map(int, input().split()))

def roll(direction):
    global dice 
    
    if direction == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        
def move(direction):
    global x, y
    tempX, tempY = x, y
    
    if direction == 4:
        tempX = x + 1
    elif direction == 2:
        tempY = y - 1
    elif direction == 1:
        tempY = y + 1
    elif direction == 3:
        tempX = x - 1
        
    if (tempX > (N - 1) or tempY > (M - 1) or tempX < 0 or tempY < 0):
        return None
    else:
        x = tempX
        y = tempY
        return maps[x][y]
    


result = []
for command in commands:
    value = move(command)
    
    if (value == None):
        continue
    
    roll(command)
    if (value != 0):
        dice[5] = value 
        maps[x][y] = 0
    else:
        maps[x][y] = dice[5] 
        
    # print(command, ' - ', value, ' : ', dice)
    result.append(dice[0])
        
        

# print(maps)
#print(commands)
for x in result:
    print(x)
    

