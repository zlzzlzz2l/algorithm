num = int(input())

for i in reversed(range(1, num + 1)):
    for s in range(num-i):
        print(" ", end='')
    for j in range(2*i-1):
        print("*", end='')
    print("\n", end='')

for i in range(2, num+1):
    for s in range(num-i):
        print(" ", end='')
    for j in range(2*i-1):
        print("*", end='')
    print("\n", end='')