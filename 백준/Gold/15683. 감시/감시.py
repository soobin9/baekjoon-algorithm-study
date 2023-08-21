import copy
import sys 

# 세로 크기 N과 가로 크기 M이
rows, cols = map(int, input().split())

boards = [[0 for _ in range(cols)] for _ in range(rows)]
cameras = [] 
for i in range(rows):
    boards[i] = list(map(int, input().split()))
    for j in range(cols):
        # 카메라 cctv에 있다면 
        if boards[i][j] in range(1,6):
            cameras.append((i,j))
        
    
# 0 : 12, 1: 3, 2: 6, 3: 9
d1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
d2 = [[1,0,1,0],[0,1,0,1]]
d3 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
d4 = [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]
d5 = [[1,1,1,1]]


##### 
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def checkCamera(camera, directions, boards):
    for key,direct in enumerate(directions):
        if direct == 1:
            nx = camera[0]
            ny = camera[1]
            while True:
                nx = nx + dx[key]
                ny = ny + dy[key]
                if nx in range(0,rows) and ny in range(0,cols) and boards[nx][ny] != 6:
                    boards[nx][ny] = '#'; 
                else:
                    break 
    # print(boards)
    
results = sys.maxsize
def dfs(cnt, boards):
    global results
    if cnt == len(cameras):
        temp = 0 
        for i in range(rows):
            for j in range(cols):
                if boards[i][j] ==0:
                    temp = temp + 1
        results = min(results, temp)
        
        # print(boards)
        return 
    
    cx, cy = cameras[cnt]
    for direction in decideDx(cx, cy):
        boardsCopy = copy.deepcopy(boards)
        checkCamera((cx,cy), direction, boardsCopy)
        dfs(cnt + 1, boardsCopy)
        
    

def decideDx(i,j):
    if boards[i][j] == 1:
        return d1
    elif boards[i][j] == 2:
        return d2
    elif boards[i][j] == 3:
        return d3 
    elif boards[i][j] == 4:
        return d4
    elif boards[i][j] == 5:
        return d5 


dfs(0, boards)
print(results)
