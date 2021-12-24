# A1
# result의 초기값으로 1을 설정하고, 앞에서부터 차례대로 더하거나 곱하기
s = input()

result = 1

for i in range(len(s)):
    if s[i] == '0' or s[i] == '1':
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)