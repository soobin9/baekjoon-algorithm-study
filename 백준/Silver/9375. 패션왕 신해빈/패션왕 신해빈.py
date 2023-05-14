testCaseNum = int(input())

for _ in range(testCaseNum):
    type = int(input())
    map = {}
    for _ in range(type):
        clothes, type = input().split()
        # print(clothes, ' : ', type)
        
        if not type in map:
            map[type] = 1
        else:
            map[type] = map[type] + 1
            
    
    count = 1        
    for type in map.keys():
        count = count * (map[type] + 1) # 1은 안 입는 케이스 
        # print(type, ' - ', map[type])
    
    print(count - 1) # 1은 전체 안 입는 케이스 
    
        
    
    