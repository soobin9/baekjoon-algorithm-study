import sys 
input = sys.stdin.readline

# 세로선의 개수 N, 가로선의 개수 M, 놓을 수 있는 위치의 개수 H 
N,M,H = map(int,input().split())
lines = [[False for _ in range(N)] for _ in range(H)]
if M == 0:
    print(0)
    exit()
    
# 사다리 정보 저장 
for i in range(M):
    a, b = map(int, input().split())
    lines[a - 1][b - 1] = True

# 사다리 타서 리턴 
def climb(start):
    end = start
    for i in range(H):
        # 사다리가 있으면  
        # print(i, start)
        # 보정 
        if start < N and lines[i][start] == True:
                start = start + 1 
        elif start > 0 and lines[i][start - 1] == True:
                start = start - 1
    
    end = start
    return end 

# 종료 체크 
def finish():
    for i in range(N):
        if climb(i) != i :
            return False
    return True
    
    
# print(lines[5])
# for i in range(H):
#     for j in range(N):
#         print(i, j)
#         print(lines[i][j], '!')

result = sys.maxsize
def dfs(lines, cnt, si, sj):
    global result
    if cnt > 3:
        return
    
    if finish():
        result = min(result, cnt)
        return
    
    if cnt > result:
        return 
    
    
        
    for i in range(si, H):
        for j in range(N - 1):
            # 마지막 행은 제외 
            if i == si and j == 0 and sj < (N - 1):
                j = sj

            if lines[i][j] == False: 
                # 연속인 경우 제거 
                if j > 0 and lines[i][j - 1] == True:
                    continue
                if j < (N-1) and lines[i][j + 1] == True:
                    continue
                
                #linesCopy = copy.deepcopy(lines)
                #linesCopy[i][j] = True 
                # j + 2 로 해서 연속으로 안 들어가게끔 함
                lines[i][j] = True
                dfs(lines, cnt + 1, i, j+2)   
                lines[i][j] = False
    
dfs(lines, 0, 0, 0)
if result == sys.maxsize :
    result = -1
print(result)
        


