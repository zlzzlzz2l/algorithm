N = input() # 정수 문자열로 입력받기
M = N # 변수 M에 N 복사
res = 0 # 더한 값
cnt = 0 # 카운트
num = "" # 새로운 수

while num != M: # 새로운 수와 M이 같지 않으면 반복
    for i in N: # 문자열만큼 반복
        res += int(i) # 정수형으로 변환해서 문자 더한 값에 저장
        if i == N[-1]: # 만약 문자열의 끝이라면
            res = str(res) # 더한 숫자 문자열로 변환
            num = N[-1] + res[-1] # N의 끝자리와 더한 값의 끝자리르 더해 num에 대입
            res = int(res) # 더한 숫자 정수로 변환
    if int(num) != int(M): # 새로운 수와 입력값이 같지 않아면
        cnt += 1 # 카운트 +1
        res = 0 # 더한 값 0으로 초기화
        N = num # N에 새로운 수 대입
    else: # 새로운 수와 입력값이 같으면
        cnt += 1 # 카운트 + 1
        break # 반복문 나가기

print(cnt)