num = int(input())

for i in range(1, num+1):
    for sp in range(num-i):
        print(" ", end='')
    for s in range(i):
        print("*", end='')
    print("")

for i in reversed(range(num)):
    for sp in range(num-i):
        print(" ", end='')
    for s in range(i):
        print("*", end='')
    print("")