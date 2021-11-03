def solution(s):
    answer = ''
    res = list(map(str, s.split(" "))) # 문자열 공백을 기준으로 리스트화
    for i in range(len(res)): # res 길이만큼 반복
        for j in range(len(res[i])): # res[i] 요소의 길이만큼 반복
            if j % 2 == 0: # 인덱스가 짝수라면
                answer += res[i][j].upper() # 해당 문자를 대문화로 변환 후 answer에 추가
            else: # 인덱스가 홀수라면
                answer += res[i][j].lower() # 해당 문자를 소문자로 변환 후 answer에 추가
        if len(res) == i+1: # 맨 마지막 요소일 때
            break # 반복문 나가기
        else: # 맨 마지막 요소가 아닐 때
            answer += " " # 띄어쓰기
    return answer

# 입출력 예시
s = "try hello world"
print(solution(s))