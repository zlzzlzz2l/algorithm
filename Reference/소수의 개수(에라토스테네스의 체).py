N = int(input())
nums = [0] * (N+1)
result = 0

for i in range(2, N+1):
    if nums[i] == 0:
        result += 1
        for j in range(2, N+1):
            if i*j > N:
                break
            nums[i*j] = 1

for i in range(2, N+1):
    if nums[i] == 0:
        result += 1
        for j in range(i, N+1, i):
            nums[j] = 1

print(result)