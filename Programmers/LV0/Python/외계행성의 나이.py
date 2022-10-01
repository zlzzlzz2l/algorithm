def solution(age):
    answer = ''
    space_age = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
    age = str(age)
    for a in age:
        for key, value in space_age.items():
            if a == value:
                answer += key

    return answer


age = 51
print(solution(age))