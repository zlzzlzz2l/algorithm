import sys # sys 모듈 불러오기

num = list(map(int, sys.stdin.readline().strip())) # 문자열 정수로 입력받기

num.sort(reverse=True) # 내림차순 정렬

for i in num:
    print(i, end="") # 출력