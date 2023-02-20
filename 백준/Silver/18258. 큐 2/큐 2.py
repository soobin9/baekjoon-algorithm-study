import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    str =  sys.stdin.readline()
    strArray = str.split()
  
    command = strArray[0]
    if len(strArray) > 1:
        args = strArray[1]
        
        
    if (command == 'push') :
        queue.append(args)
    elif (command == 'pop') :
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif (command == 'size') :
        print(len(queue))
    elif (command == 'empty') :
        if not queue:
            print(1)
        else:
            print(0)
    elif (command == 'front') :
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif (command == 'back') :
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    
