def solution(arr):
    answer = ['a']
    for a in arr:
        if a == answer[-1]:
            continue
        else:
            answer.append(a)
    answer.remove('a')
    return answer

# 입출력 예시
arr = [4,4,4,3,3]
print(solution(arr))