from itertools import combinations

def solution(nums):
    answer = 0
    res = list(combinations(nums, 3)) # 조합으로 3개 숫자 뽑기
    for i in res:
        cnt = 0 # 소수 아닌 수들의 개수
        n = sum(i) # res[i] 집합의 합
        for j in range(2, n): # 뽑은 숫자의 합이 소수인지 판별
            if n % j == 0: # 다른 숫자로 나눠지면 소수 x
                cnt += 1 # cnt = cnt + 1 즉, 소수 아닌 수 카운트
                break # for문 나가기
        if cnt == 0: # 만약 다른 숫자로 안나눠졌다면 cnt의 값은 0이기 때문에 즉, 소수가 있기 때문에
            answer += 1 # 소수 개수

    return answer

# 입출력 예시
nums = [1,2,7,6,4]
print(solution(nums))