N = int(input())
num = list(map(int, input().split()))
num.sort()

result = 0 # 그룹 수
count = 0 # 그룹에 포함된 모험가 수

for i in num: # 공포도를 낮은 것부터 확인
    count += 1 # 현재 그룹에 모험가 추가
    if count >= i: # 모험가 수가 공포도보다 크거나 같다면
        result += 1 # 그룹 수 증가
        count = 0 # 그룹에 포함된 모험가 초기화

print(result)