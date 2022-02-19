import heapq as hq
import sys

pq = []
for _ in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    if num:
        hq.heappush(pq, (abs(num), num))
    else:
        print(hq.heappop(pq)[1] if pq else 0)