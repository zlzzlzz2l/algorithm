def solution(a, b):
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    mon = 0
    for d in date[:a-1]:
        mon += d
    mon += b
    res = mon % 7
    return day[res-1]

# 입출력 예시
a = 12
b = 12
print(solution(a, b))