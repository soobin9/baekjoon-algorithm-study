import sys

stack = [] # stack = array : 복잡하게 클래스로 만들 필요 없다 
def push(data):
  stack.append(data)

def pop():
  if (empty()):
    print(-1)
  else:
    lastIndex = len(stack) -1
    print(stack.pop(lastIndex)) # remove (value), pop (index)
  
def size():
  print(len(stack))

def empty():
  if len(stack) == 0:
    return 1
  else:
    return 0
  
def top():
  if (empty()):
    print(-1)
  else:
    lastIndex = len(stack) -1
    print(stack[lastIndex])
  
# 명령어 수 받기 
num = int(sys.stdin.readline()) #input 사용할 시 시간 초과 
for i in range(num):
  str = sys.stdin.readline()
  strArray = str.split()
  
  command = strArray[0]
  if len(strArray) > 1:
    args = strArray[1]
    
  if (command == 'push'):
    push(args)
  elif (command == 'pop'):
    pop()
  elif (command == 'size'):
    size()
  elif (command == 'empty'):
    print(empty())
  elif (command == 'top'):
    top()
    

    