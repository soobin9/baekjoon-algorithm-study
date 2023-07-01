import sys
input = sys.stdin.readline 

N = int(input())


meetingList = list()
for _ in range(N):
    meetingList.append(list(map(int, input().split())))
    

dp = [0] * (N + 1)

for i in range(1, N + 1):
    time = meetingList[i - 1][0]
    price = meetingList[i - 1][1]

    # 회의 참석할 경우 
    if (i + time - 1) <= len(meetingList):
        dp[i + time - 1] = max(dp[i + time - 1], dp[i - 1] + price)
        
    ### 회의 참석 안할 경우, 그 전날 값을 가져옴 
    if dp[i - 1] > dp[i]:
        dp[i] = dp[i - 1]
    ###
    # print(i, ' >> ', dp)

print(max(dp))


    

    