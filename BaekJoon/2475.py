num = list(map(int, input().split(" "))) # 유호번호 입력받고 리스트로 선언
result = 0
for i in num: # num 요소만큼 반복
    result += i*i # 요소를 제곱한 뒤 result에 저장

result = result % 10 # 제곱의 합을 10으로 나눈 나머지
print(result) # 출력