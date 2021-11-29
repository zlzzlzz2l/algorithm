x, y = map(int, input().split())

M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = {1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT", 0: "SUN"}
day = 0

for m in M[:x-1]:
    day = day + m

day = day + y

print(d[day % 7])