
N = int(input())
nList = list(map(int, input().split()))

max = -1000000
min = 1000000
for i in nList:
        # 현재값이 최소값보다 더 작다면
        if (i < min):
                min = i

        # 현재값이 최대값보다 더 크다면
        if (i > max):
                max = i


print(min, max)