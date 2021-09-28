from itertools import combinations

N, M = map(int, input().split()) # 카드의 개수, 해당 값을 넘지 않는 카드의 값

data = list(map(int, input().split())) # 카드에 쓰여 있는 수

result = list(combinations(data, 3)) # 카드에 쓰여 있는 숫자 중에 순서 상관없이 3개 뽑기.

total = [] # 뽑은 3개를 더한 값을 넣을 리스트

for i in result:
    if sum(i) <= M: # 더한 값 중에 M과 같거나 작은 값이 있다면
        total.append((sum(i))) # 리스트에 넣어준다

total = set(total) # 중복을 제거하기 위해 집합 자료형으로 바꾸기
total = sorted(list(total)) # 집합 자료형을 리스트로 바꾼 후 오름차순 정렬

print(total[-1]) # 맨 마지막 값이 출력값