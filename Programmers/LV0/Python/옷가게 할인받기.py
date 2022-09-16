def solution(price):
    sale = 0
    answer = 0
    if 100000 <= price <= 299999:
        sale = price * 0.05
    elif 300000 <= price <= 499999:
        sale = price * 0.1
    elif 500000 <= price <= 1000000:
        sale = price * 0.2

    answer = price - sale
    return int(answer)


price = 580000
print(solution(price))