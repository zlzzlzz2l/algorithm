def solution(arr):
    if len(arr) <= 1: # 길이가 1보다 작거나 같다면
        answer = [-1] # answer에 [-1] 대입
    else: # 길이가 2 이상이라면
        res = arr[0] # 제일 작은 수를 arr[0] 요소라고 가정
        for i in range(1,len(arr)):
            if res > arr[i]: # 다른 요소들이 res보다 작을 때마다
                res = arr[i] # res의 값을 다른 요소값으로 바꾼다.
        arr.remove(res) # res 안에 가장 작은 값이 들어가 있어서 그 값을 arr에서 제거해준다.
        answer = arr # answer에 arr을 대입
    return answer

# 입출력 예시
arr = [3, 5, 11, 14, 2, 25]
print(solution(arr))