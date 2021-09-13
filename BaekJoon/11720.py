import sys
N = int(input())
num = input()
l = []
if N == len(num):
    for i in str(num):
        l.append(int(i))

print(sum(l))