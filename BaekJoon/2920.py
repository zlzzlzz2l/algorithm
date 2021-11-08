N = list(map(int, input().split())) # 입력값 받기

arr1 = [1, 2, 3, 4, 5, 6, 7, 8] # 오름차순
arr2 = [8, 7, 6, 5, 4, 3, 2, 1] # 내림차순

if arr1 == N: # 오름차순과 같다면
    print("ascending")
elif arr2 == N: # 내림차순과 같다면
    print("descending")
else: # 둘 다 아니라면
    print("mixed")