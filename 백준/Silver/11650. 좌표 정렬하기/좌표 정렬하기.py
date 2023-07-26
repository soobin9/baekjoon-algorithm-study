N = int(input())

list = [] 
for i in range(N):
    list.append(tuple(map(int, input().split())))
    
    
list = sorted(list, key=lambda item: (item[0], item[1]))
for i in range(N):
    print(*list[i])