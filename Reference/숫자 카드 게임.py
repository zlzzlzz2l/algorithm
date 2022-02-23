N, M = map(int, input().split()) # N: 행, M: 열
min_num = 0
result = 0
for i in range(N):
    card = list(map(int, input().split()))
    min_num = min(card)
    result = max(result, min_num) # 가장 작은 수들 중에서 가장 큰 수 찾기

print(result)
