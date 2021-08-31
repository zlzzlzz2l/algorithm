num1, num2 = map(int, input().split())

A = list(map(int, input().split(" ")))

for i in A:
    if num2 > i:
        print(i, end=" ")