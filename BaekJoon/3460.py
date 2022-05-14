T = int(input())

for _ in range(T):
    num = int(input())
    l = []
    s = -1
    while num >= 1:
        if num % 2 == 1:
            s += 1
            l.append(s)
            num = num // 2
        else:
            s += 1
            num = num // 2
    print(' '.join(map(str, l)))