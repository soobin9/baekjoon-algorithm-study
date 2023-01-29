
sticks = input()

stack = []
count = 0
for i in range(len(sticks)):
    cur = sticks[i]
    
    # ( 만나면 stack push 
    if (cur == '('):
        stack.append(cur)
        
    # 최상단이 (이고 그 다음이) 이면 size 추가 
    # ) 만나면 1 추가 
    elif (cur == ')'):
        stack.pop()
        
        if (sticks[i - 1] == '('):
            count += len(stack)
        else:
            count = count + 1
            
    # print(i, ' : ', cur, ' - ', count)
            
print(count)

