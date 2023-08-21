N = int(input())

arr = [] 
for i in range(N):
    arr.append(int(input()))
   
arr.sort()

# 선택 정렬 
for cur in range(N):
    min = arr[cur]
    
    for i in range(cur + 1, N):
        if min > arr[i]:
            min = arr[i] 
    
    # 맨 앞에 넣기 
    arr.remove(min)
    arr.insert(cur, min)
    # print(arr)


for i in range(N):
    print(arr[i])
