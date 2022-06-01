s_length = int(input())
sentence = input()
count_i = 0
count_2 = 0

if len(sentence) != s_length:
    exit()
else:
    for i in sentence:
        if i == 'e':
            count_i += 1
        else:
            count_2 += 1
    if count_2 > count_i:
        print("2")
    elif count_2 < count_i:
        print("e")
    else:
        print("yee")