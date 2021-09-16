def solution(lottos, win_nums):
    a = 0
    b = 0
    answer = []
    for i in range(len(lottos)):
        if lottos[i] == 0:
            b = b + 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                a = a + 1 # 같은 수

    c = a + b

    if a == 2:
        a = 5
    elif a == 3:
        a = 4
    elif a == 4:
        a = 3
    elif a == 5:
        a = 2
    elif a == 6:
        a = 1
    else:
        a = 6

    if c == 2:
        c = 5
    elif c == 3:
        c = 4
    elif c == 4:
        c = 3
    elif c == 5:
        c = 2
    elif c == 6:
        c = 1
    else:
        c = 6

    print(lottos.count(0))

    answer.append(c)
    answer.append(a)
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)