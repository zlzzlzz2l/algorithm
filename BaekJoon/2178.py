from collections import deque
N, M = map(int, input().split())
miro = [input() for _ in range(N)]

# L R U D
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs():
    chk = [[False] * M for _ in range(N)] # M x N으로 check
    chk[0][0] = True # 출발점 True
    dq = deque()
    dq.append((0, 0, 0))
    while dq:
        x, y, cnt = dq.popleft()
        total_cnt = cnt + 1

        if y == M - 1 and x == N - 1:
            return total_cnt

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid_coord(nx, ny) and miro[nx][ny] == '1' and not chk[nx][ny]:
                chk[nx][ny] = True
                dq.append((nx, ny, total_cnt))

print(bfs())