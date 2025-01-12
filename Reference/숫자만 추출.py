word = input()
result = 0
a = 1
for w in word:
    if w.isdigit():
        result = result * 10 + int(w)

print(result)

count = 0
for i in range(1, result + 1):
    if result % i == 0:
        count += 1

print(count)