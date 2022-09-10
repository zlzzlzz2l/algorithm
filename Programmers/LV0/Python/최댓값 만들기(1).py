def solution(numbers):
    numbers = sorted(numbers)
    answer = numbers[-1] * numbers[-2]
    return answer


numbers = [0, 31, 24, 10, 1, 9]
print(solution(numbers))