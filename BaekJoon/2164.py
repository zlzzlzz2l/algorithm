from collections import deque

N = int(input())
# nums = deque(i for i in range(1, N+1))
nums = deque(range(1, N+1))

while len(nums) != 1:
    nums.popleft()
    # nums.append(nums[0])
    # nums.popleft()
    nums.append(nums.popleft())  # 주석 처리 부분 합칠 수 있다. nums의 맨 앞에 있는 숫자를 빼고 그 숫자를 뒤에 추가

print(nums[0])