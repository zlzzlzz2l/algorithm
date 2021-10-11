E, S, M = map(int, input().split()) # 입력 받기

year = 0 # 출력 값

year_e, year_s, year_m = 0, 0, 0 # 입력 값과 비교할 값

while [E, S, M] != [year_e, year_s, year_m]: # 입력 값과 비교할 값 같지 않으면 반복
    year += 1 # 연도 + 1
    if year_e >= 15: # 지구 범위 초과
        year_e = 0
    if year_s >= 28: # 태양 범위 초과
        year_s = 0
    if year_m >= 19: # 달 범위 초과
        year_m = 0
    year_e += 1
    year_s += 1
    year_m += 1

print(year)