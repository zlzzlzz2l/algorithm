import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(now, group):
    visited[now] = group

    for nxt in graph[now]:
        if not visited[nxt]:
            a = dfs(nxt, -group)
            if not a:
                return False
        elif visited[nxt] == visited[now]:
            return False
    return True


T = int(input())
for _ in range(T):
    u, v = map(int, input().split())
    graph = [[] for _ in range(u + 1)]
    visited = [False] * (u + 1)

    for _ in range(v):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        graph[dest].append(src)


    for i in range(1, u+1):
        if not visited[i]:
            result = dfs(i, 1) # 방문한 정점이 아닐 때 dfs 수행
            if not result:
                break

    print("YES" if result else "NO")