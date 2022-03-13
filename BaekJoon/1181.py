N = int(input()) # 단어의 개수

word = [input() for _ in range(N)]
set_word = set(word) # 단어 중복 제거
set_word_list = []

for w in set_word:
    set_word_list.append((len(w), w)) # 단어의 길이와 단어를 집합으로 묶어 리스트에 추가

result = sorted(set_word_list) # 오름차순 정리

for word_len, word in result:
    print(word) # 단어 출력