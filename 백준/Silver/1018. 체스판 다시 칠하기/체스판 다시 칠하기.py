import sys
# N, M 

N, M = map(int, input().split())

board = [[None for _ in range(M)] for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(M):
        board[i][j] = line[j]
        

Bboards = ['BWBWBWBW', 'WBWBWBWB'] * 4      
Wboards = ['WBWBWBWB', 'BWBWBWBW'] * 4      
def countByStart(x, y, start):
    if start == 'B':
        checkBoard = Bboards
    elif start == 'W':
        checkBoard = Wboards
    
    count = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != checkBoard[i][j]:
                count += 1
    
    return count
            
        
    
        

# 8 * 8 로 자르기 
results = sys.maxsize
for i in range(N):
    for j in range(M):
        if i + 8 <= N and j + 8 <= M:
            switched = min(countByStart(i, j, 'B'), countByStart(i, j, 'W'))
            results = min(results, switched)
            # print(i, j, switched)

print(results)


    
    
    