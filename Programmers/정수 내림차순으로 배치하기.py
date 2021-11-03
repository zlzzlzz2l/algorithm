def solution(n):
    word = ""
    res = list(map(int, str(n))) # 정수 n의 각 자리수를 리스트화
    res.sort(reverse=True) # 내림차순 정렬
    for i in res:
        word += str(i) # 리스트에 있는 요소들을 word에 추가
    answer = int(word) # word를 정수로 변환하여 answer에 대입
    return answer

# 입출력 예시
n = 118372
print(solution(n))