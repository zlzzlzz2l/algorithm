def solution(s):
    res = len(s) // 2 # 가운데 문자열 인덱스
    if len(s) % 2 == 0: # 문자열 길이가 짝수일 때
        answer = s[res-1:res+1] # 짝수면 인덱스 기준 앞 문자까지 가져오기
    else: # 문자열 길이가 홀수일 때
        answer = s[res]

    return answer

# 입출력 예시
s = "qwerer"
print(solution(s))