def solution(price, money, count):
    sum = 0
    for c in range(1, count + 1):
        sum += (c * price)

    if sum >= money:
        answer = sum - money
    else:
        answer = 0

    return answer

# 입출력 예시
price = 3
money = 20
count = 4
print(solution(price, money, count))