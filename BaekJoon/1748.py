N = int(input()) # N 입력

result = "" # 숫자 합칠 빈 문자열 생성

for i in range(1, N+1): # 1부터 N까지 반복
    result += str(i) # 정수형 i를 문자열 i로 변환 후 빈 문자열에 대입

print(len(result))