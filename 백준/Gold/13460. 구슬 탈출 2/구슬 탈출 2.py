import sys
input = sys.stdin.readline 

rows, cols = map(int, input().split())

# . 빈칸 
# # 공이 이동할 수 없는 장애물 또는 벽
# 0 구멍의 위치
# R - 빨간 구슬의 위치 
# B - 파란 구슬의 위치 

board = []
for i in range(rows):
    board.append(list(input().rstrip()))
    
    for j in range(cols):
        if board[i][j]=='B':
            blue = ([i,j])
        if board[i][j]=='R':
            red = ([i,j])

    
# 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(startX, startY, check):
    count = 0
    
    while True:
        if board[startX + dx[check]][startY + dy[check]] != '#' and board[startX][startY] != 'O':
            startX += dx[check]
            startY += dy[check]
            count += 1
        else:
            break
 
    return startX, startY, count
    
 
results = 11
def dfs(rx,ry,bx,by,count):
    global results 
    if count > 10:
        return 
    
    for check in range(4):
        nrx,nry,nrc = move(rx, ry, check)
        nbx,nby,nbc = move(bx, by, check)
        
        # print(count, ' >> ', check, ' >>', rx, ry, nrx, nry)
        # print(count, ' >> ', check, ' >>', bx, by, nbx, nby)
        
        # print(*board, sep='\n')
        # print('##')
        if board[nbx][nby] == 'O':
            continue 
        if board[nrx][nry] == 'O':
            results = min(results, count)
            continue 
        
        # R, B 가 동일한 경우 
        if nrx == nbx and nry == nby:
            if nrc > nbc:
                nrx = nrx - dx[check]
                nry = nry - dy[check]
            elif nbc > nrc:
                nbx = nbx - dx[check]
                nby = nby - dy[check]
                
        dfs(nrx, nry, nbx, nby, count + 1)

dfs(red[0], red[1], blue[0], blue[1],  1)
if results == 11:
    print(-1)
else:
    print(results)
            
            
        
        
        
        
        

