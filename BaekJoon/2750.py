N = int(input()) # 입력할 수의 개수
num = [] # 입력한 수 넣을 리스트
for i in range(0, N): # 입력할 수의 개수만큼 반복
    num.append(int(input())) # 입력받은 수를 리스트에 삽입
    if i == N-1: # 맨 마지막 수를 삽입한다면
        result = sorted(num) # 리스트를 오름차순 정렬 후 변수에 대입

for i in range(0, N): # 입력한 수만큼 반복
    print(result[i]) # 원소 하나씩 출력
