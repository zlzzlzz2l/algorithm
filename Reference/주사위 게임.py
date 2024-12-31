N = int(input())
result = 0

# for _ in range(N):
#     nums = list(map(int, input().split()))
#     if nums[0] == nums[1] == nums[2]:
#         total = 10000 + nums[0] * 1000
#     elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
#         if nums[0] == nums[1]:
#             total = 1000 + nums[0] * 100
#         elif nums[1] == nums[2]:
#             total = 1000 + nums[1] * 100
#         else:
#             total = 1000 + nums[2] * 100
#     else:
#         total = max(nums) * 100
#
#     if result < total:
#         result = total

for _ in range(N):
    nums = input().split()
    nums.sort()
    a, b, c = map(int, nums)

    if a == b == c:
        total = 10000 + a * 1000
    elif a == b or a == c:
        total = 1000 + a * 1000
    elif b == c:
        total = 1000 + b * 1000
    else:
        total = c * 100

    if result < total:
        result = total

print(result)