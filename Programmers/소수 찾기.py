def solution(n):
    arr = [] # 2부터 n+1까지 나눴을 때 나누어 떨어지는 수 리스트
    rm = [] # 1과 자기 자신을 제외한 수로 나눠지는 수 리스트

    # 2부터 n+1까지 나눴을 때 나누어 떨어지는 수 arr 리스트에 추가
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i % j == 0:
                arr.append(i) # 1개 담긴 숫자는 소수

    # 소수가 아닌 숫자 rm 리스트에 추가 및 중복 제거
    for i in range(1, len(arr)-1):
        if arr[i-1] == arr[i]:
            rm.append(arr[i])
        rm = set(rm)
        rm = list(rm)

    # 입력값에서 1과 rm의 길이를 빼면 소수 개수가 나옴
    answer = n - 1 - len(rm)
    return answer

# 입출력 예시
n = 5
print(solution(n))