N = int(input())

for i in reversed(range(N)):
    for s in range(i+1):
        print("*", end="")
    print("")