N = int(input())
meetings = []

for i in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])
    
# print(meetings)
meetings.sort(key=lambda x: (x[1], x[0])) 
# 회의 끝나는 시간 오름차순, 같다면, 희의 시작하는 시간 오름차순 
# print(meetings)


# (회의 끝나는 시간 - 회의 시작되는 시간)이 작은 것부터 고른다.
# 회의가 시작되는 시간이 작은 값부터 고른다.
# 회의가 끝나는 시간이 작은 값부터 고른다. 


# 탐욕법 
# 회의 끝나는 시간이 빠를 수록 더 많은 회의를 고를 수 있다 
# 끝나는 시간 이후부터 가장 빨리 시작되는 회의를 골라야 한다. 

result = 0
endTime = 0
for i in range(len(meetings)):
    # 시작시간이 현재 종료시간보다 길면 
    if endTime <= meetings[i][0]:
        endTime = meetings[i][1]
        result = result + 1
        
print(result)
    