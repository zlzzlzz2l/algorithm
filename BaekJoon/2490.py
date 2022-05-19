for _ in range(3):
    y = list(map(int, input().split()))
    s = sum(y)
    if s == 0:
        print("D")
    elif s == 1:
        print("C")
    elif s == 2:
        print("B")
    elif s == 3:
        print("A")
    else:
        print("E")
