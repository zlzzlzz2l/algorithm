word = input()
num = 0
result = ''

for i in word:
    if i.isdigit():
        num += int(i)
    else:
        result += i

total = ''.join(sorted(result))

if num > 0:
    total += str(num)

print(total)