def solution(seoul):
    for answer in seoul:
        if answer == "Kim":
            idx = seoul.index(answer) # 김서방 인덱스
            break
    return f'김서방은 {idx}에 있다' # String으로 반환


# 입출력 예시
seoul = ["Jane", "Kim"]
print(solution(seoul))