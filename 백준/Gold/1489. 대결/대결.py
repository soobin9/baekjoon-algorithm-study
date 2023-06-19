
# i : a 뒤에서부터, b 뒤에서부터 시작
def dynamic(dp, a, b, i, j):
    if i < 0 or j <0:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    if a[i] < b[j]:
        dp[i][j] = dynamic(dp, a, b, i, j - 1)
    elif a[i] > b[j]:
        dp[i][j] = dynamic(dp, a, b, i - 1, j - 1) + 2 
    # 동점일때 분기태움 
    else:
        dp[i][j] = max(dynamic(dp, a, b, i, j - 1), dynamic(dp, a, b, i - 1, j - 1) + 1)
    
    return dp[i][j]


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# https://sdev.tistory.com/660﻿
a.sort()
b.sort()

# https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
dp = [[None] * n for _ in range(n)]
print(dynamic(dp, a, b, n - 1, n - 1))


    
        
        