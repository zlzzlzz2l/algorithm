def solution(s):
    word = s.split(" ") # 공백을 기준으로 s를 리스트화
    print(word)
    for i in range(len(word)): # 리스트의 길이만큼 반복
        word[i] = word[i][:1].upper() + word[i][1:].lower() # 맨 첫글자는 대문자로 나머지는 소문자로 바꾼 뒤

    return ' '.join(word) # 공백을 기준으로 join을 리턴

s = "3people unFollowed me"
print(solution(s))