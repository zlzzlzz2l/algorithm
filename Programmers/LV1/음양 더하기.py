def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] is True:
            answer += abs(absolutes[i])
        elif signs[i] is False:
            answer += -absolutes[i]

    return answer


absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))