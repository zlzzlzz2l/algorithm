def solution(x):
    x = str(x) # x를 문자열로 치환
    nums = 0 # x의 자리수 더해서 저장할 변수
    for i in x: # 문자열 x의 요소만큼 반복
        nums += int(i) # 요소를 정수로 치환해서 num에 더해준다

    if int(x) % nums == 0: # 정수 x를 자릿수합으로 나눴을 때 나머지가 0이라면
        answer = True # 하샤드 수 O
    else: # 0이 아니라면
        answer = False # 하샤드 수 X

    return answer

# 입출력 예시
x = 13
print(solution(x))