from itertools import permutations

N, M = map(int, (input().split()))

data = [i for i in range(1, N+1)]

result = list(permutations(data, M))

for i in result:
    print(' '.join(map(str, i)))