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

# A2
# result2의 초기값을 s2[0]으로 설정하고, s[1]부터 더하거나 곱하기
s2 = input()
result2 = int(s2[0])

for i in range(1, len(s)):
    num = int(s2[i])
    if num <= 1:
        result2 += num
    else:
        result2 *= num

print(result2)