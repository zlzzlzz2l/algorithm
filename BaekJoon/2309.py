from itertools import combinations # 조합 라이브러리

heights = [int(input()) for _ in range(9)]

for i in combinations(heights, 7): # 7개씩 뽑은 튜플로 반복
    if sum(i) == 100: # 해당 튜플 값이 100이라면
        for h in sorted(i):
            print(h) # 원소 하나씩 출력
        break
    else:
        continue