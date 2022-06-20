count = 0

for j in range(8):
    c = list(input())
    if j % 2 == 0:
        for i in range(0, 7, 2):
            if c[i] == 'F':
                count += 1
    else:
        for i in range(1, 8, 2):
            if c[i] == 'F':
                count += 1
print(count)