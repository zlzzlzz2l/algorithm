# A1
# 단순히 n이 k로 나눠질 때, 아닐 때

n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)

# A2
# k로 나눠지는 가장 가까운 수를 만들어 한 번에 1을 빼는 방법

n, k = map(int, input().split())
cnt = 0


while True:
    target = (n // k) * k # k로 나눠지는 n과 가까운 가장 가까운 수
    cnt += (n - target) # 1을 빼는 연산을 한 번에
    n = target
    if n < k:
        break
    cnt += 1
    n //= k

cnt += (n - 1) # k보다 n이 작을 때는 무조건 -1이니까
print(cnt)
