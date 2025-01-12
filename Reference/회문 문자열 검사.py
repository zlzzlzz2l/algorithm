N = int(input())

# Solve 1
for i in range(N):
    word = input()
    word = word.lower()

    result = ""

    for w in range(len(word)-1, -1, -1):
        result += word[w]

    if word == result:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

# Solve2
for i in range(N):
    word = input()
    word = word.lower()
    size = len(word)

    for j in range(size // 2):
        if word[j] != word[-1-j]:
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")

# Solve3
for i in range(N):
    word = input()
    word = word.lower()

    if word == word[::-1]: # 문자열 역순
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")