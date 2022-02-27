from collections import deque
N, M, V = map(int, input().split())

nums = [[0] * (N+1) for _ in range(N+1)]
chk = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    nums[a][b] = nums[b][a] = 1

def dfs(V):
    chk[V] = True
    print(V, end=' ')

    for nxt in range(1, N+1):
        if not chk[nxt] and nums[V][nxt]:
            dfs(nxt)

def bfs(V):
    dq = deque()
    dq.append(V)
    chk[V] = True
    while dq:
        row = dq.popleft()
        print(row, end=' ')
        for nxt in range(1, N+1):
            if chk[nxt] and nums[V][nxt]:
                dq.append(nxt)
                chk[nxt] = False

dfs(V)
print()
bfs(V)
