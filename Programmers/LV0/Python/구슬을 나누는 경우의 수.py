from itertools import combinations

def solution(balls, share):
    answer, num, m_multi = 1, 1, 1
    nums = balls - share
    for n in range(1, balls + 1):
        answer *= n
    for n in range(1, nums + 1):
        num *= n
    for m in range(1, share + 1):
        m_multi *= m

    return answer // (num * m_multi)


balls = 3 # 머쓱이가 갖고 있는 구슬의 개수
share = 2 # 친구들에게 나누어줄 구슬의 개수
print(solution(balls, share)) # 3