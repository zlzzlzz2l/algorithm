def solution(n):
    answer = 0
    n = str(n) # 자연수 n을 문자열로 치환
    for i in n: # 문자열 n만큼 반복
        answer += int(i) # 문자열 요소를 정수로 치환후 answer에 대입
    return answer

# 입출력 예시
n = 987
print(solution(n))