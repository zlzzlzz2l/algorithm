def solution(array, commands):
    answer = []
    for i in range(len(commands)): # commands의 길이만큼 반복
        arr = array[commands[i][0]-1:commands[i][1]] # array에서 commands 요소들의 첫번째 두번째 원소 기준으로 슬라이싱
        arr = sorted(arr) # 오름차순 정렬
        answer.append(arr[commands[i][2]-1]) # commands 요소들의 세번째 원소로 arr 요소 출력
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))