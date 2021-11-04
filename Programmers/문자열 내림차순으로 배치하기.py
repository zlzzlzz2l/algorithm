def solution(s):
    answer = "".join(sorted(list(s), reverse=True)) # 문자열 리스트화 시킨 후 내림차순 정렬
    return answer

# 입출력 예시
s = "Zbcdefa"
print(solution(s))