word = list(input())

res = []
for i in range(len(word)):
    res.append(''.join(word))
    word.remove(word[0])

print('\n'.join(sorted(res)))