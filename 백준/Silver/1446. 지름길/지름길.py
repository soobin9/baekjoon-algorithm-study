from collections import defaultdict, deque 
import sys

# 지름길의 개수, 고속도로의 길이 
N, D = map(int, input().split())

roads = defaultdict(list)
for i in range(N):
    start, end, length = map(int, input().split())
    roads[start].append((end, length))
    
# 운전해야 하는 거리의 최솟값 
# bfs 혹은 dp 
queue = deque()
queue.append([0, 0])

results =  sys.maxsize
while queue:
    offset, offsetLength = queue.popleft() 
    if offset > D:
        continue
    
    if offset == D:
        results = min(results, offsetLength)
        
    if roads.get(offset) != None:
        for end, length in roads[offset]:
            queue.append([end, offsetLength + length])
            
    
    queue.append([offset + 1, offsetLength + 1])
    
print(results)
        
        
    

