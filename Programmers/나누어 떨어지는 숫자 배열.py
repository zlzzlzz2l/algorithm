def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0: # arr의 요소가 divisor로 나뉠 때
            answer.append(i) # answer에 i를 추가
        else: # 안나뉠 때
            continue

    if len(answer) == 0: # answer의 길이가 0이라면 == 나뉘는 수가 없을 때
        answer.append(-1) # answer에 -1 추가

    return sorted(answer)

# 입출력 예시
arr = [3,2,6]
divisor = 10
print(solution(arr, divisor))