###
#
#자주 나오는 단어일수록 앞에 배치한다.
#해당 단어의 길이가 길수록 앞에 배치한다.
#알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
#
###


# N : 영어 지문에 나오는 단어의 개수 
# M : 외울 단어의 기준이 되는 

import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
dict = {}
for i in range(N):
    word = input().strip()
    if (len(word) >= M):
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    

# 빈도수 내림차순, 길이 내림차순 
dict = sorted(dict.items(), key = lambda item: (-item[1], -len(item[0]), item[0]))

for word, frequency in dict:
    print(word)
    