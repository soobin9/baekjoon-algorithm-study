from collections import defaultdict 
import sys
import heapq

# 헛간, 길 
N, M = map(int, input().split()) 

roads = defaultdict(list)
for i in range(M):
    s, e, w = map(int, input().split())
    
    # 양방향이기 때문에 각각 넣어줌 
    roads[s].append((e, w))
    roads[e].append((s, w))
    
queue = []
visited = [False] * (N + 1)
results = [sys.maxsize] * (N + 1)

# 1번부터 시작 
results[1] = 0
heapq.heappush(queue, (1, 0))

while queue:
    offset, offsetWeight = heapq.heappop(queue) 
    
    if results[offset] < offsetWeight:
        continue 
        
    for e, w in roads[offset]:
        if (results[e] > (offsetWeight + w)):
            results[e] = offsetWeight + w
            heapq.heappush(queue, (e, offsetWeight + w))
            
            
print(results[N])