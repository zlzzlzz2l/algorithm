result = [] # 나머지 넣어줄 리스트 선언
for i in range(10): # 10번
    N = int(input()) # 숫자 입력
    change = N % 42 # 입력받은 숫자를 42로 나눈 나머지를 change에 선언
    result.append(change) # 나머지를 result 리스트에 넣기

print(len(set(result))) # 리스트 중복 제거 후 길이 출력 == 서로 다른 나머지 몇 개인지 출력