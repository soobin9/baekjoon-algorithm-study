import sys
from collections import deque


N = int(input())

queue = deque([])

for i in range(N):
    queue.append(i + 1)

while(len(queue) > 1):
    # 제일 위 숫자 버림 
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue.popleft())