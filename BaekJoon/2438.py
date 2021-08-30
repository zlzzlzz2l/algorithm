num = int(input())

for i in range(1, num + 1):
    for s in range(i):
        print("*", end='')
    print("\n", end='')
