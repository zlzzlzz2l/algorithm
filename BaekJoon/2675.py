T = int(input()) # 테스트 케이스 입력받기

for i in range(T): # 테스트 케이스만큼 반복
    R, S = map(str, input().split(" ")) # R: 반복횟수, S: 문자열
    result = '' # 빈문자열 선언
    S = list(S) # 문자열 리스트화
    for i in S: # 문자열 요소 반복
        result += i*int(R) # 요소를 반복횟수만큼 반복한 후 result에 저장
    print(result)