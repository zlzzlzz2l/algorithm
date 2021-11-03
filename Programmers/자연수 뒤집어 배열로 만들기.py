def solution(n):
    answer = []
    res = list(map(int, str(n))) # 정수 n의 각 자리수 리스트화
    for i in range(len(res)-1, -1, -1): # res의 맨 뒤 요소부터 차례대로 answer 리스트에 추가
        answer.append(res[i])
    return answer

# 입출력 예시
n = 12345
print(solution(n))