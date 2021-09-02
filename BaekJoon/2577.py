abc = []
res = [0] * 10
num = 1

for i in range(3):
    abc.append(int(input()))
    num = num * abc[i]

calc = list(map(int, str(num)))

for key in range(0, len(calc)):
    if calc[key] == 0:
        res[0] += 1
    elif calc[key] == 1:
        res[1] += 1
    elif calc[key] == 2:
        res[2] += 1
    elif calc[key] == 3:
        res[3] += 1
    elif calc[key] == 4:
        res[4] += 1
    elif calc[key] == 5:
        res[5] += 1
    elif calc[key] == 6:
        res[6] += 1
    elif calc[key] == 7:
        res[7] += 1
    elif calc[key] == 8:
        res[8] += 1
    else:
        res[9] += 1

for i in res:
    print(i)