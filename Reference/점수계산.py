N = int(input())
nums = list(map(int, input().split()))
result, count = 0, 0

for num in nums:
    if num == 1:
        count += 1
        result += count
    else:
        count = 0

print(result)