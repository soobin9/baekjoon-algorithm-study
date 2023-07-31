import math, sys
input = sys.stdin.readline 

H, W, N, M = map(int, input().split())

# arr = [[None for _ in range(W)] for _ in range(H)]
# arr[0][0] = True 
# results = 0
# # H , N 
# # W, M 
# for i in range(H):
#     for j in range(W):
#         # print(i, j, arr[i-N-1][j-M-1])
#         if (i - N - 1) in range(0, H) and arr[i-N-1][j] == True:
#                 arr[i][j] = True
#         if (j - M - 1) in range(0, W) and arr[i][j-M-1] == True:
#                 arr[i][j] = True
#         if arr[i][j] == True:
#             results = results + 1

rows = math.ceil(W/(M + 1))
cols = math.ceil(H/(N + 1)) 

# print(rows, cols)                
print(rows * cols)
# print(*arr)