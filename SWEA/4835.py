T = int(input()) # 테스트 케이스 개수

for i in range(T): # 테스트 케이스만큼 반복
    result = []  # 더한 값 저장
    N, M = map(int, input().split())  # 정수 개수 및 구간의 개수
    t = N - M + 1 # 가까운 수끼리 더하는 횟수
    num = list(map(int,input().split())) # 정수 입력

    for n in range(0, t): # 가까운 수끼리 더하는 횟수만큼 반복
        total = sum(num[n:n+M]) # 0부터 시작해서 M씩 더하기
        result.append(total) # 더한 값 result 리스트에 삽입

    result.sort() # 오름차순 정렬
    print(f"#{i+1} {result[-1]-result[0]}") # 최대값에서 최소값 빼기
