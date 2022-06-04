import sys

while True:
    count = 0
    sentence = sys.stdin.readline().strip()
    if len(sentence) > 255:
        break
    elif sentence == '#':
        break
    for s in sentence:
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
            count += 1
    print(count)