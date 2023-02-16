
N, K = map(int, input().split())
num = input()


stack = []
cnt = K
for i in num:
    # 현재 i가 stack에 있는 값보다 크다면 제거 
    while (cnt > 0 and len(stack) > 0 and stack[len(stack) - 1] < i): 
        stack.pop(len(stack) - 1)
        cnt = cnt - 1
    stack.append(i)


# 반례 : 54321 / 1 => 마지막까지 삭제 안한 케이스 고려해야함 
answer = ''
for i in range(len(stack) - cnt):
    answer += stack[i]
print(answer)
