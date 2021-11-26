import sys
N = sys.stdin.readline().strip()

for i in range(0, len(N), 10):
    print(N[i:i+10])