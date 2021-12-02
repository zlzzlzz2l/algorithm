N = int(input()) # 입력값 받기

for i in range(N+1):

    res = 0 # 생성자 변수
    list_num = list(map(int, str(i))) # num 리스트화

    for j in range(len(list_num)): # num 리스트화 시킨 값 더해주는 루프
        res += list_num[j] # res에 각각의 자리 더해주기

    res += i # res에 num 더하기

    if res == N: # 생성자가 입력값과 같다면
        result = i # 결과값을 result에 대입
        break # 루프 탈출
    elif i == N: # 생성자 없는 경우
        result = 0
    else:
        continue # 반복

print(result) # 결과값 출력