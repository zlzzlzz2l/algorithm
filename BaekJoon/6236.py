import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
days = []
for _ in range(N):
    days.append(int(readline()))

answer, left, right = sum(days), 0, sum(days)

while left <= right:
    mid = (left + right) // 2
    count, money = 0, 0
    lack = False

    for d in days:
        if mid - d < 0:
            lack = True
            break
        elif money - d < 0:
            money = mid
            count += 1
        money -= d

    if not lack:
        if count <= M:
            right = mid - 1
            if mid < answer:
                answer = mid
        elif count > M:
            left = mid + 1

    else:
        left = mid+1

print(answer)