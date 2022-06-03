import sys
sentence = ''
while True:
    sentence = sys.stdin.readline().strip()
    if sentence == 'END':
        break
    elif len(sentence) > 500:
        break
    else:
        for s in sentence[::-1]:
            print(s, end="")
        print()