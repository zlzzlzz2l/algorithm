from collections import Counter
word_count = []
word = input()
for i in range(len(word)):
    word_count.append(word[i].upper())

sorted_word = sorted(word_count)
mode_dict = Counter(sorted_word)
modes = mode_dict.most_common()

if len(word) > 1:
    if modes[0][1] == modes[1][1]:
        print("?")
    else:
        mod = modes[0][0]
        print(mod)
else:
    mod = modes[0][0]
    print(mod)