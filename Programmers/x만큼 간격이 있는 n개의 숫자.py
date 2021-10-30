def solution(x, n):
    answer = [x*i for i in range(1, n+1)] # 1부터 n+1번 반복해서 x에 i를 곱해준다
    return answer

# 입력값
# x: 2, n: 5, answer: [2, 4, 6, 8, 10]
# x: 4, n: 3, answer: [4,8,12]
# x: -4, n: 2, answer: [-4, -8]