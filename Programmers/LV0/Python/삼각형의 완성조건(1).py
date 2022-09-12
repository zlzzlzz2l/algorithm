def solution(sides):
    sides = sorted(sides)
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2
    return answer


sides = [199, 72, 222]
print(solution(sides))