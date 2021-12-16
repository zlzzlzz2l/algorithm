from math import gcd

def solution(arr):
    answer = 0
    for i in range(1, len(arr)): # 길이만큼 반복
        max_num = gcd(arr[i-1], arr[i]) # 최대공약수 구하기
        arr[i] = arr[i-1] * arr[i] // max_num # 최소공배수 구하고 arr[i]에 그 값을 대입
        if i == len(arr)-1: # 원소의 개수와 i가 같다면
            answer = arr[i] # 모든 원소의 최소공배수를 다 구한 것으로 answer에 대입
    return answer

# 입출력 예시
arr = [2,6,8,14]
print(solution(arr))
    