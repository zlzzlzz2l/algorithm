import math


def solution(denum1, num1, denum2, num2):
    answer = []

    res_num = int(num1 * num2 / math.gcd(num1, num2))
    if denum1 != res_num:
        a = res_num // num1
        denum1 = denum1 * a
    if denum2 != res_num:
        b = res_num // num2
        denum2 = denum2 * b

    res_denum = denum1 + denum2

    if math.gcd(res_denum, res_num) != 1:
        res = math.gcd(res_denum, res_num)
        res_denum //= res
        res_num //= res
        answer.append(res_denum)
        answer.append(res_num)
    else:
        answer.append(res_denum)
        answer.append(res_num)
    return answer


print(solution(2, 4, 1, 3))