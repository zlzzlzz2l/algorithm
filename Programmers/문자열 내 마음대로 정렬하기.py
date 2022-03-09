def solution(strings, n):
    answer = []
    n_list = []
    for string in strings:
        a = string[n] + string
        n_list.append(a)

    n_list.sort()

    for i in n_list:
        answer.append(i[1:])
    return answer

# 입출력 예시
strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))