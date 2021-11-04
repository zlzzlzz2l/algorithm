T = int(input()) # 테스트 케이스

for i in range(T):
    N = int(input()) # 정수의 개수
    num = list(map(int, input().split())) # 정수 리스트화
    arr = [] # 정렬된 리스트
    for j in range(len(num)):
        if j % 2 == 0: # 인덱스가 짝수일 때
            arr.append(max(num)) # num에서 가장 큰 값 arr에 추가
            num.remove(max(num)) # num에서 가장 큰 값 제거
        else: # 인덱스가 홀수일 때
            arr.append(min(num)) # num에서 가장 작은 값 arr에 추가
            num.remove(min(num)) # num에서 가장 작은 값 제거

    res = " ".join(map(str, arr[:10]))
    print(f"#{i+1} {res}") # 숫자 10개까지 출력