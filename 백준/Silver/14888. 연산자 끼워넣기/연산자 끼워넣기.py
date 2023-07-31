import sys

N = int(input()) # 숫자 
list = []

for num in input().split():
    list.append(int(num))
    
# 덧셈, 뺄셈, 곱셈, 나눗셈
plus, minus, multiple, divide = map(int,input().split())

maxResult = - sys.maxsize
minResult = sys.maxsize
def dfs(cur, result, plus, minus, multiple, divide):
    start = cur 
    next = cur + 1
    
    # print(cur, result)
    if cur == (N - 1):
        global maxResult, minResult
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)
    
    if plus > 0:
        dfs(next, result + list[next], plus - 1, minus, multiple, divide)
    if minus > 0:
        dfs(next, result - list[next], plus, minus - 1, multiple, divide)
    if multiple > 0:
        # print('here', next, result * list[next], plus, minus, multiple - 1, divide)
        dfs(next, result * list[next], plus, minus, multiple - 1, divide)
    if divide > 0:
        dfs(next, int(result / list[next]), plus, minus, multiple, divide - 1)
        
# 0부터 dfs 
dfs(0, list[0], plus, minus, multiple, divide)

print(maxResult)
print(minResult)
        
        