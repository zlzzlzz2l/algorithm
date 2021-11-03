from math import gcd # 최대공약수 라이브러리

# 라이브러리 이용X
def solution(n, m):
    answer = []
    n_num = [] # n의 약수 리스트
    m_num = [] # m의 약수 리스트
    res = 1
    for i in range(1, n+1):
        if n % i == 0: # n을 1부터 n까지 나눴을 때 나머지가 0인 것이 n의 약수
            n_num.append(i)
    for j in range(1, m+1):
        if m % j == 0: # m을 1부터 m까지 나눴을 때 나머지가 0인 것이 m의 약수
            m_num.append(j)

    for i in n_num:
        for j in m_num:
            if i == j: # n과 m의 약수가 같다면 두 수의 최대공약수 될 약수
                answer.append(i)

    for i in range(1, len(answer)):
        if answer[i-1] < answer[i]:
            res = answer[i] # 공통된 약수중 제일 큰 수가 최대공약수

    n = n // res # 최대공약수로 나눠주기
    m = m // res
    t = n * m * res # 최대공배수

    answer = [res, t]

    return answer

# 라이브러리 이용
def solution2(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

# 입출력 예시
n = 4
m = 8

print(solution(n, m))
print(solution2(n, m))