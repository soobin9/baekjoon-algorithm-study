N = int(input())

# results = [[' ' for _ in range(N)] for _ in range(N)]


# 잘못된 풀이 - *****, * *, ***** 반복 후 가운데 제거 
pattern = [['*','*','*'], ['*', ' ', '*'], ['*','*','*']]
def stars(n):
    if n == 1:
        return ['*']
    
    mid = int(n/3)
    arr=stars(mid)
    star = []
    
    for v in arr:
        star.append(v * 3)
    for v in arr:
        star.append(v + ' ' * mid + v)
    for v in arr:
        star.append(v * 3)

    return star

val = stars(N)
for i in range(N):
    print(val[i])
    
    
    
    
    
    
    