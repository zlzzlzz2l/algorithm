def solution(s):
    answer = ''
    nums = sorted(list(map(int, s.split(" "))), reverse=True)
    answer += str(nums[-1]) + " "
    answer += str(nums[0])
    return answer

# 입출력 예시
s = "1 2 3 4"
print(solution(s))