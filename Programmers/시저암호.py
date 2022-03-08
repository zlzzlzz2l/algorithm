def solution(s, n):
    answer = ''
    for w in s:
        if w.isspace():
            answer += w
            continue
        sum = ord(w) + n
        if w.isupper():
            if sum >= 65 and sum <= 90:
                answer += chr(sum)
            else:
                cnt = sum - 90
                answer += chr(64 + cnt)
        if w.islower():
            if sum >= 97 and sum <= 122:
                answer += chr(sum)
            else:
                cnt = sum - 122
                answer += chr(96 + cnt)
    return answer

# 입출력 예시
s = "A  B"
n = 27
print(solution(s, n))