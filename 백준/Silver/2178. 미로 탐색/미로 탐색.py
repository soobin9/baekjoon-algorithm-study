import sys 
from collections import deque

# N, M (0,0)에서 출발하여 (N,M)까지 ... 
rows, cols = map(int, input().split())

miro = [[None for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    miro[i] = list(map(int, input()))

### input 종료 

visited = [[False for _ in range(cols)] for _ in range(rows)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = sys.maxsize
# def dfs(si, sj, cnt):
#     global result
#     if si == (rows - 1) and sj == (cols - 1):
#         print(si,sj,cnt)
#         result = min(result, cnt)
#         return 
    
#     visited[si][sj] = True 
#     for i in range(4):
#         if (si + dx[i]) in range(0,rows) and (sj + dy[i]) in range(0, cols):
#             if visited[si + dx[i]][sj + dy[i]] == False and miro[si + dx[i]][sj + dy[i]] == 1: 
#                 dfs(si + dx[i], sj + dy[i], cnt + 1)

# dfs(0, 0, 1)
# print(result)   


def bfs(si, sj):
    q = deque()
    q.append([si,sj])
    
    while q:
        si, sj = q.popleft()
        for i in range(4):
            if (si + dx[i]) in range(0,rows) and (sj + dy[i]) in range(0, cols):
                if visited[si + dx[i]][sj + dy[i]] == False and miro[si + dx[i]][sj + dy[i]] == 1: 
                    q.append([si + dx[i], sj + dy[i]])
                    visited[si + dx[i]][ sj + dy[i]] = True 
                    miro[si + dx[i]][sj + dy[i]] = miro[si][sj] + 1 
                    
bfs(0,0)
print(miro[rows -1][cols - 1])
                    
            
        
    

    
