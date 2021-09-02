N = int(input())
numList = list(map(int, input().split(" ")))
min = numList[0]
max = numList[0]

for i in range(1, N):
    if max < numList[i]:
        max = numList[i]
    else:
        continue

for t in range(1, N):
    if min > numList[t]:
        min = numList[t]
    else:
        continue

print(min, max)