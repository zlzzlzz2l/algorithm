N = int(input())
result = 666
while True: # 무한 반복
    if '666' in str(result): # 만약 666이란 문자열이 문자열(first)안에 있으면
        N = N - 1 # N을 1 감소시키고
        if N == 0: # 만약 N 이 0이면
            break # 반복문을 탈출한다.
    result = result + 1 #result의 값을 1 증가시킨다.
print(result)