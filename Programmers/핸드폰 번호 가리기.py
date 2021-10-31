def solution(phone_number):
    answer = ''
    phone_number = list(phone_number) # 문자열 -> 리스트
    for i in range(len(phone_number)-4): # 문자열길이 - 4 (맨 뒤 4글자는 안바꾸기 위해서)
        phone_number[i] = "*" # 맨 뒤 4글자 제외하고 *로 바꾼다
    for i in phone_number:
        answer += i # 리스트 요소를 answer에 추가
    return answer

# 입출력 예시
phone_number = "027778888"
print(solution(phone_number))