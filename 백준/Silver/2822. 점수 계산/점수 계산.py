
list = []
for _ in range(8):
    list.append(int(input()))
    
list = sorted(
    enumerate(list), 
    key = lambda item: -item[1]
)

sum = 0
values = []
for i in range(5):
    sum = sum + list[i][1]
    values.append((list[i][0] + 1)) # 0 -> 1번부터 세기때문에 
    
print(sum)
print(*sorted(values))