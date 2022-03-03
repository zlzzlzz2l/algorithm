import sys
input = sys.stdin.readline
N, M = map(int, input().split())

nums = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: x-1, map(int, input().split()))
    nums[u][v] = nums[v][u] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if nums[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)