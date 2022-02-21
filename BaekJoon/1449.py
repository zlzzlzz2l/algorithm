N, L = map(int, input().split())

location = list(map(int, input().split()))
location.sort()

tape = 1
start = location[0]
end = start + L - 0.5
for l in location:
    if end >= l:
        continue
    else:
        tape += 1
        end = l + L - 0.5

print(tape)