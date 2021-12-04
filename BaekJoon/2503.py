from itertools import permutations # 순열 라이브러리

N = int(input())
num = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)) # 미리 3개씩 뽑아두기
removeCount = 0
print(num)
for _ in range(N):
    n, s, b = map(int, input().split()) # 입력값 받기
    removeCount = 0 # num[0]부터 시작하기 위해서
    n = list(str(n)) # 입력받은 숫자 문자열로 나열
    for i in range(len(num)):
        strike = 0
        ball = 0
        i -= removeCount
        for j in range(3):
            if num[i][j] == n[j]: # n[j]와 num[i][j]가 같다면(자리가 같다는 얘기)
                strike += 1 # strike
            elif n[j] in num[i]: # num안의 숫자 중에 n[j]가 있다면(숫자를 포함한다는 얘기)
                ball += 1 # ball

        if strike != s or ball != b: # 입력받은 s,b와 strike,ball이 같지 않으면
            num.remove(num[i]) # 관련없는 숫자이기 때문에 제거
            removeCount += 1 # num[0]부터 시작하기 위해서 count

print(len(num))