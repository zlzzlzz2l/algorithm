def solution(s):
    s = list(s.lower()) # 문자열 소문자로 바꾼 후 리스트화
    if s.count("p") == s.count("y"): # p의 개수랑 y의 개수가 같다면
        answer = True # true
    else: # 같지 않다면
        answer = False # false
    return answer

# 입출력 예시
s = "Pyy"
print(solution(s))