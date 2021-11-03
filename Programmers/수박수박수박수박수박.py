def solution(n):
    word = "수박" * 10000 # n의 길이만큼 반복
    answer = word[:n] # 0부터 n까지 출력
    return answer

# 입출력 예시
n = 4
print(solution(n))