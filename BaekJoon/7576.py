from collections import deque

M, N = map(int, input().split()) # M, N 입력받기
graph = [list(map(int, input().split())) for _ in range(N)] # 토마토

# L R U D
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
res = 0

def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append([nx, ny])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dq.append([i, j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))

print(res - 1)