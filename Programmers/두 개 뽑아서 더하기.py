from itertools import combinations # 조합 라이브러리

def solution(numbers):
    answer = []
    data = list(combinations(numbers, 2)) # numbers중 2개 뽑기
    for i in data:
        answer.append(sum(i)) # 2개 뽑은 값을 더해서 answer에 삽입
    answer = set(answer) # 중복 제거
    answer = sorted(list(answer)) # 오름차순 리스트
    return answer

# 입출력 예시
numbers = [5,0,2,7]
print(solution(numbers))