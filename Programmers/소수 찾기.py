def solution(n):
    graph = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if graph[i] == True:
            for j in range(i+i, n+1, i):
                graph[j] = False

    result = [i for i in range(2, n+1) if graph[i] == True]
    return len(result)

# 입출력 예시
n = 5
print(solution(n))