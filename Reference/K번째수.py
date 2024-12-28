T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    result = nums[s-1:e]
    result.sort()
    print(f"#{i+1} {result[k-1]}")