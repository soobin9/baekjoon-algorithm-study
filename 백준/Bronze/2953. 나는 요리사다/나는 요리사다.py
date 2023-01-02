# 점수 받아서 저장
score_list = [list(map(int, input().split())) for _ in range(5)]


# 기준점 구하기
sum = 0
rank = 1
for i in range(4):
        sum += score_list[0][i]


for i in range(1, 5):
        score = 0
        for j in range(4):
                score += score_list[i][j]

        if (score > sum):
                sum = score
                rank = i + 1

print(rank,  sum)