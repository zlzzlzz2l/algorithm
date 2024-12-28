A, B = map(int, input().split(" "))
result = []

for i in range(1, A+1):
    if A % i == 0:
        result.append(i)

if len(result) == 0 or len(result) < B:
    print(-1)
else:
    print(result.pop(B-1))