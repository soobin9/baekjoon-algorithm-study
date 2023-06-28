N = int(input())

# debug 
def mprint(meetingList):
    for i in range(len(meetingList)):
        print(*meetingList[i])
        
results = list()
def dfs(start, current, history):
    if (start >= len(meetingList)):
        # print(start, ' : ', history, ' > ', current)
        results.append(current)
        return
    
    # 현재 미팅을 할 수 있다면 
    next = start + meetingList[start][0]
    if (next <= len(meetingList)):
        dfs(next, current + meetingList[start][1], history + str(start))
    
    for i in range(start + 1, next):
        dfs(i, current, history)
    

meetingList = list()
for _ in range(N):
    meetingList.append(list(map(int, input().split())))

dfs(0, 0, '')
# print(results)
results.sort()
print(results[-1])
# mprint(meetingList)  


