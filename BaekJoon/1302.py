import sys

books = {}
for _ in range(int(input())):
    b = sys.stdin.readline().strip()
    if b in books:
        books[b] += 1
    else:
        books[b] = 1

max_sell = []

for k, v in books.items():
    if v == max(books.values()):
        max_sell.append(k)

print(sorted(max_sell)[0])