def check(word):
    s = []  # 괄호 담을 리스트
    for t in word:
        if t == "{" or t == "(": # 왼쪽 괄호가 문자열 안에 있을 때
            s.append(t) # 괄호 담을 리스트에 추가한다
        elif t == "}" or t == ")": # 오른쪽 괄호가 문자열 안에 있을 때
            if len(s) == 0: # 스택 안에 괄호가 없을 때
                return 0
            elif (t == "}" and s[-1] != "{") or (t == ")" and s[-1] != "("): # 괄호가 다를 때
                return 0
            else:
                s.pop(-1) # 스택에서 꺼냄

    if s: # empty list에 괄호가 남아있다면
        return 0
    return 1


T = int(input()) # 테스트 케이스

for i in range(T): # 테스트 케이스만큼 반복
    word = input() # 문자열 입력값 받기
    result = check(word)
    print(f"#{i+1} {result}")