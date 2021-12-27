# 입력값 받기
N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

result = 0

for i in range(len(coin), 0, -1): # 역순으로 반복
    result += K // coin[i-1] # 나눈 몫을 result에 추가
    K %= coin[i-1] # K를 나눈 나머지로 대입
    if K == 0: # K가 0이라면
        break # 반복 탈출

print(result)