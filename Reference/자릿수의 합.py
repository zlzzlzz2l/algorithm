N = int(input())
nums = list(map(int, input().split()))
max = -2147000000

def digit_sum(x):
    tmp = str(x)
    value = 0
    for j in tmp:
        value += int(j)
    return value

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

for num in nums:
    value = digit_sum(num)
    if max < value:
        max = value
        result = num

print(result)