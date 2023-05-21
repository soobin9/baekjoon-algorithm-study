expression = input()

expressionArr = expression.split('-')

first = 0; 
# 처음 마이너스가 나오기 전까지 모두 더해주고, 그다음 모두 빼준다. 
# 반례 50 - (50) - (50) 
for num in expressionArr[0].split('+'):
  first = first + int(num)

result = first
if len(expressionArr) > 1:
  for numArray in expressionArr[1:]:
    group = 0
    for num in numArray.split('+'):
      group = group + int(num)
    result = result - group
  
print(result)
