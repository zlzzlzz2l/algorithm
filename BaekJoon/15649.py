from itertools import permutations # 순열 라이브러리

N, M = map(int, (input().split())) # N과 M 입력 받기

data = [i for i in range(1, N+1)] # 1부터 N까지 데이터를 리스트화

result = list(permutations(data, M)) # data 리스트 안에서 서로 다른 M개의 데이터 뽑기

for i in result:
    print(i)
    print(' '.join(map(str, i))) # 튜플 값을 문자열로 바꾼 뒤 문자열로 합친다. 튜플 -> 문자열