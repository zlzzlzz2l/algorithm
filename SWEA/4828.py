T = int(input()) # 테스트 케이스 수

for i in range(1, T+1): # 테스트 케이스 수만큼 반복
    N = int(input()) # 양수 개수 입력
    num = list(map(int, input().split())) # 양수를 리스트로 입력
    result = max(num) - min(num) # 큰 원소에서 작은 원소 빼기
    print(f"#{i} {result}") # 결과값 출력
