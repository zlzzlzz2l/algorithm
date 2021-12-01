N = int(input()) # 테스트 케이스

for num in range(N):
    result = 0 # str1과 str2가 같지 않을 때 0 출력하는 result 변수

    # 문자열 입력받기
    str1 = input()
    str2 = input()

    # str1과 str2의 인덱스
    i = 0
    j = 0

    # 인덱스가 str1과 str2의 길이보다 작을 때까지 반복
    while j < len(str1) and i < len(str2):
        if str2[i] != str1[j]: # 일치하지 않으면
            i = i - j # str2의 인덱스 한 칸 뒤로 이동
            j = -1 # str1은 맨 앞으로 가기
        i += 1
        j += 1

    if j == len(str1): # 인덱스와 문자열의 길이가 같다면 같은 문자열을 포함하고 있다는 뜻
        result = 1

    print(f"#{num+1} {result}")