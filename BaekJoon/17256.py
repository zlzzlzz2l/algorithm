a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * 3

b[0] = c[0] - a[2]
b[1] = c[1] // a[1]
b[2] = c[2] - a[0]

print(' '.join(map(str, b)))