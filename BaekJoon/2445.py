num = int(input())

for i in range(1, num + 1):
    for j in range(i):
        print("*", end='')
    for s in range(num-i):
        print(" ", end='')
    for n in range(num-i):
        print(" ", end='')
    for p in range(i):
        print("*", end='')
    print("\n", end='')

for i in reversed(range(num)):
    for j in range(i):
        print("*", end='')
    for s in range(num-i):
        print(" ", end='')
    for n in range(num-i):
        print(" ", end='')
    for p in range(i):
        print("*", end='')
    print("\n", end='')