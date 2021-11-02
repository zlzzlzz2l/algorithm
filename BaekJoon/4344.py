N = int(input()) # 테스트 케이스

for i in range(N): # 테스트 케이스만큼 반복
    stu = list(map(int, input().split())) # 학생수, 학생 점수 리스트로 입력
    total = 0 # 학생 점수 총합
    avg = 0.0 # 평균
    cnt = 0 # 평균 넘는 학생 수
    for j in range(1, len(stu)): # 리스트 첫번째 요소는 학생 수여서 제외하고 반복
        total += stu[j] # 학생 점수 더하기
    avg = total / stu[0] # 총점에서 학생수로 평균

    for j in range(1, len(stu)): # 리스트 첫번째 요소는 학생 수여서 제외하고 반복
        if stu[j] > avg: # 학생 점수 중에 평균을 넘는다면
            cnt += 1 # 평균 넘는 학생 수 카운트 + 1
    avg_up = (100 / stu[0]) * cnt # 학생들 비율 구하기

    print("%0.3f%%" %avg_up)
