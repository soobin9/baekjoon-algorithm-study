T = int(input()) # 테스트 케이스 

# x시 y로 읽는 것이 가능한지 
# 시는 0시에서 23시까지, 분은 0분에서 59분까지가 유효
def checkWithTime(hour, minute):
    if hour in range(24) and minute in range(60):
        return 'Yes'
    else:
        return 'No'

#  월은 1월에서 12월까지가 유효하다. 
# 1월, 3월, 5월, 7월, 8월, 10월, 12월은 1일에서 31일까지가 유효하고, 
# 4월, 6월, 9월, 11월은 1일에서 30일까지가 유효하며, 2월은 1일에서 29일까지
def chechWithDate(month, day):
    if month not in range(1, 13):
        return 'No'
    elif month in [1,3,5,7,8,10,12] and day in range(1,32):
        return 'Yes'
    elif month in [4,6,9,11] and day in range(1,31):
        return 'Yes'
    elif month == 2 and day in range(1,30):
        return 'Yes'
    else:
        return 'No'

# range 계산시 마지막은 포함안됨, 따라서 +1 씩 해주어야 함 
for i in range(T):
    first, second = map(int, input().split())
    print(checkWithTime(first, second), chechWithDate(first, second))
    