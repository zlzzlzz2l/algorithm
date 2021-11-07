A, B = map(int, input().split(" ")) # 입력값 받기

# 뒤집은 수 넣어줄 변수
num1 = ""
num2 = ""

# A와 B를 문자열로 치환 후 뒤집어서 리스트화
A = list(reversed(str(A)))
B = list(reversed(str(B)))

# A와 B 리스트에 있는 요소를 변수에 대입
for i in range(3):
    num1 += A[i]
    num2 += B[i]

if int(num1) > int(num2): # num1이 num2보다 크다면
    print(num1) # num1 출력
else: # num1이 num2보다 작다면
    print(num2) # num2 출력