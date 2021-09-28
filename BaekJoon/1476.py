E, S, M = map(int, input().split()) # 입력 받기

year = 0 # 출력 값

year_e, year_s, year_m = 0, 0, 0 # 입력 값과 비교할 값

while True: # 무한 루프
    if year_e == E and year_s == S and year_m == M: # 비교할 값과 입력 값이 같다면
        print(year) # 우리가 알고 있는 연도 출력
        break # 루프 빠져나오기
    else: # 같지 않다면
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