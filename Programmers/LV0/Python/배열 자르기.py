def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer


numbers = [1, 3, 5]
num1 = 1
num2 = 2
print(solution(numbers, num1, num2))