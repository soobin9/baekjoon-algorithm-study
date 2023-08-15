# 두 개의 정수 N과 K 
# N : 온도 측정한 전체 날짜의 수 
# K : 연속적인 날짜의 수 


N, K = map(int, input().split())
degrees = list(map(int, input().split()))
    
dp = [None for _ in range(N)]
dp[0] = degrees[0]
dp[1] = degrees[0] + degrees[1]

    
for i in range(1, N):
    if i < K:
        dp[i] = dp[i - 1] + degrees[i]
        #print(dp)
    else:
        dp[i] = dp[i - 1] - degrees[i - K] + degrees[i]
        #print(2, i, dp)
   
result = max(dp[K-1:])
    
print(result)
        
        