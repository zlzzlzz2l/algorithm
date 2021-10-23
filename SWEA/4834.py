def sorting(num, N):
    temp = [0] * (N+1)
    for i in range(0, len(num)):
        temp[num[i]] += 1

    return temp


T = int(input())
for i in range(T):
    N = int(input())
    num = list(map(int, input()))
    t = sorting(num, max(num))
    a = t[0]
    for n in range(1, len(t)):
        if a < t[n] or a == t[n]:
            a = t[n]
            b = n
            print(n, a)
    if max(t) > 1:
        result = b
        c = a
    else:
        result = max(num)
        c = 1
    print(f"#{i+1} {result} {c}")