import math
N = int(input())
nums = list(map(int, input().split()))

# 평균
avg_math = int(sum(nums) / N + 0.5)

min = 2147000000 # 정수형에서 가장 큰 값

for idx, num in enumerate(nums):
    distance = abs(avg_math - num)
    if distance < min:
        min = distance
        score = num # 거리가 같은 점수가 있을 수도 있으니
        result = idx + 1
    elif distance == min: # 거리가 같을 때
        if num > score:
            score = num
            result = idx + 1

print(avg_math, result)