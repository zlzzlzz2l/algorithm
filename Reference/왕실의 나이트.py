# A1
start = input()

mx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

type_one = [[2, -1], [-2, -1], [2, 1], [-2, 1]]
type_two = [[1, 2], [-1, 2], [1, -2], [-1, -2]]

x, y = mx.index(start[0])+1, int(start[1])
count = 0
for one in type_one:
    if x + one[0] < 1 or y + one[1] < 1 or x + one[0] > 8 or y + one[1] > 8:
        continue
    else:
        count += 1

for two in type_two:
    if x + two[0] < 1 or y + two[1] < 1 or x + two[0] > 8 or y + two[1] > 8:
        continue
    else:
        count += 1

print(count)

# A2
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# A1과 다르게 8가지 방향을 모두 리스트에 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_column <= 8 and next_row <= 8 and next_column >= 1:
        result += 1

print(result)