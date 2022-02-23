N = int(input())

plan = input().split()
x, y = 1, 1

type = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in plan:
    for t in range(len(type)):
        if type[t] == p:
            nx = x + dx[t]
            ny = y + dy[t]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)