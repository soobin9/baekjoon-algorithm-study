import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

# for b in B:
#     if b >= Amid and b in A[int(N/2):]:
#         print('1')
#     elif b < Amid and b in A[:int(N/2)]:
#         print('1')
#     else:
#         print('0')

for b in B:
    left = 0
    right = N - 1
    mid = int((left + right)/2)
    find = False
    while left <= right:
        #print(b, '>>', left, right, mid)
        if b == A[mid]:
            find = True 
            break
        elif b > A[mid]:
            left = mid + 1
        elif b < A[mid]:
            right = mid - 1 
            
        mid = int((left + right)/2)
        #print(mid)
        
    if find == True:
        print(1)
    else:
        print(0)
        
        
        
        
        
        
        
        
        
        
        