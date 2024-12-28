from itertools import combinations

N, K = map(int, input().split())
nums = list(map(int, input().split()))
result = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            result.add(nums[i] + nums[j] + nums[m])

result = list(result)
result.sort(reverse=True)
print(result[K-1])