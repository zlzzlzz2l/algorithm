N, M = map(int, input().split())
nums = [0] * (N+M+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        value = nums.pop(i + j)
        value += 1
        nums.insert(i+j, value)
        # nums[i+j] += 1

max_value = max(nums)

for i in range(N+M+1):
    if nums[i] == max_value:
        print(i, end=" ")