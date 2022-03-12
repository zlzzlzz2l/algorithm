import sys
input = sys.stdin.readline

def dfs(now):
    visited[now] = True
    nxt = nums[now]
    if not visited[nxt]:
        dfs(nxt)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    cnt = 0

    for start in range(1, N+1):
        if not visited[start]:
            dfs(start)
            cnt += 1

    print(cnt)