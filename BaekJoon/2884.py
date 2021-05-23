h, m = input().split()
h = int(h)
m = int(m)

if h == 0:
    h = 24 * 60
else:
    h = h * 60

total = h + m - 45

h = total // 60

if h == 24:
    h = 0
else:
    h

m = total % 60

print(h, m)