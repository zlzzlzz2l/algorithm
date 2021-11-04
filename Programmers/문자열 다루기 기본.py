def solution(s):
    if len(s) == 4 or len(s) == 6: # 길이가 4 또는 6인지
        if s.isdigit(): # isdigit(): 숫자로만 이루어졌는지
            answer = True
        else: # 숫자로만 이루어져있지 않을 때
            answer = False
    else: # 길이가 4 또는 6이 아닐 때
        answer = False
    return answer

# 입출력 예시
s = "12345"
print(solution(s))