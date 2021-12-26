# A1
# 입력값 받기
N, M, K = map(int, input().split())
num = list(map(int, input().split()))

# 내림차순 정렬
num.sort(reverse=True)

# result: 더한 값, count: 더한 횟수
result = 0
first = num[0]
second = num[1]
count = 0

for _ in range(M): # M만큼 반복
    result += first # 제일 큰 값을 더해준다.
    count += 1 # 횟수 증가
    if count % K == 0: # 횟수를 K로 나눴을 때의 나머지가 0이라면(큰 수를 K만큼 더했다는 뜻)
        result += second # 그 다음 큰 값을 더해준다
        count += 1
    if count == M: # 횟수가 M과 같다면(숫자가 총 더해지는 횟수와 같기 때문에)
        break # 반복 탈출

print(result)

# A2
# 입력값 받기
N, M, K = map(int, input().split())
num = list(map(int, input().split()))

# 내림차순 정렬
num.sort()
first = num[N-1]
second = num[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)
