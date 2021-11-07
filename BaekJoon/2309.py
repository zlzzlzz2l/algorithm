from itertools import combinations # 조합 라이브러리

a = [] # inpurt값 담을 리스트
for i in range(9):
    n = int(input()) # 9개의 값 입력
    a.append(n) # 입력된 값 리스트 추가

result = list(combinations(a, 7)) # 원소 중에 7개 뽑기

for i in result: # 7개씩 뽑은 튜플로 반복
    if sum(i) == 100: # 해당 튜플 값이 100이라면
        i = sorted(i) # 튜플 오름차순 정렬
        for s in range(len(i)):
            print(i[s]) # 원소 하나씩 출력
        break
    else:
        continue