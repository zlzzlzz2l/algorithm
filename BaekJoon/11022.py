import sys

num = int(input())

for key in range(num):
    a, b = sys.stdin.readline().rstrip().split()
    print("Case #%d: %d + %d = %d" %
          (key + 1, int(a), int(b), int(a) + int(b)))
