def solution(numbers):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9] # numbers의 모든 수
    return sum(num) - sum(numbers) # 1-9까지의 합에서 numbers의 합 빼기

# 입출력 예시
numbers = [5, 8, 4, 0, 6, 7, 9]
print(solution(numbers))