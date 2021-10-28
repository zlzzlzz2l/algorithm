def solution(new_id):
    answer = ""
    # 1단계
    new_id = new_id.lower()

    #2단계
    characters = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = ''.join(x for x in new_id if x in characters)

    # 3단계
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # 4단계
    new_id = new_id.strip(".")

    # 5단계
    if new_id == "":
        new_id += "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip(".")

    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    return answer

new_id = "z-+.^."

print(solution(new_id))