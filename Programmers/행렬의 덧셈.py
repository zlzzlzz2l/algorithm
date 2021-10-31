def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): # arr1의 길이만큼 반복
        num = [] # 더한 값 넣어줄 리스트 생성
        print(len(arr1[0]))
        for j in range(len(arr1[0])): # arr1[0]의 길이만큼 반복
            num.append(arr1[i][j] + arr2[i][j]) # 같은 위치에 있는 요소를 더해서 num 리스트에 추가
        answer.append(num) # num 리스트에 있는 요소를 다시 answer 리스트에 추가

    return answer

# 입출력 예
arr1 = [[1,2],[2,3]]
arr2 = 	[[3,4],[5,6]]

print(solution(arr1, arr2))