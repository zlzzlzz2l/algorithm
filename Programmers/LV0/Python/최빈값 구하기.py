from collections import Counter

def solution(array):
    if len(array) == 1:
        return array[0]
    else:
        answer = Counter(array).most_common(2)
        if answer[0][1] is answer[1][1]:
            return -1
        return answer[0][0]

array = [1, 2, 3, 0]
print(solution(array))