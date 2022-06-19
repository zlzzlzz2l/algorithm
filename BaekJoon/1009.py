# T1 시간 초과
import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    result = (a**b)
    num = result % 10
    print(num)

# T2 성공
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    res_a = a % 10

    if res_a == 0:
        print(10)
    elif res_a in [1, 5, 6]:
        print(res_a)
    elif res_a in [4, 9]:
        res_b = b % 2
        if res_b == 0:
            print(res_a * res_a % 10)
        else:
            print(res_a)
    else:
        res_b = b % 4
        if res_b == 0:
            print(res_a**4 % 10)
        else:
            print(res_a**res_b % 10)