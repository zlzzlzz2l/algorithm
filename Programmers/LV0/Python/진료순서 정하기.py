def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        result = sorted_emergency.index(emergency[i])
        answer.append(result+1)
    return answer


emergency = [30, 10, 23, 6, 100]
print(solution(emergency))