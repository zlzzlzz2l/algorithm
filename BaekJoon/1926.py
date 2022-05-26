from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# U D L R
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, a, b):
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0
    count = 1

    while dq:
        x, y = dq.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
                count += 1
    return count

paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))