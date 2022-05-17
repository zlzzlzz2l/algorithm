T = int(input())

for _ in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    print(sum(num))