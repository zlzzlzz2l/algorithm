N = int(input())
nums = list(map(int, input().split()))

# 숫자를 뒤집을 때, 문자열로 변환하는 과정
# def reverse(num):
#     reverse_num = ""
#     # Method 1
#     for n in reversed(str(num)):
#         reverse_num += n
#     # Method 2
#     for n in range(len(str(num))-1, -1, -1):
#         reverse_num += str(num)[n]
#     return int(reverse_num)

# 숫자를 뒤집을 때, 문자열로 변환하지 않는 과정
def reverse(num):
    reverse_num = 0
    while num > 0:
        t = num % 10
        reverse_num = reverse_num * 10 + t
        num = num // 10
    return int(reverse_num)


# def isPrime(reverse_num):
#     count = 0
#     for n in range(1, reverse_num+1):
#         if reverse_num % n == 0:
#             count += 1
#
#     return True if count == 2 else False

def isPrime(reverse_num):
    if reverse_num == 1:
        return False
    for n in range(1, reverse_num//2+1):
        if reverse_num % n == 0:
            return False
    else:
        return True


for n in nums:
    reverse_num = reverse(n)
    if isPrime(reverse_num):
        print(reverse_num, end=" ")