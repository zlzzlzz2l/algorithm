import heapq
import sys

n = int(input()) # 숫자 개수
h = [] # 리스트(힙)

for _ in range(n):
    num = int(sys.stdin.readline()) # 숫자 입력받기
    if num == 0: # 0일 때
        if not h: # 힙에 아무것도 없을 때
            print(0) # 0출력
        else:
            print(heapq.heappop(h)) # 힙에서 원소 삭제 후 출력
    else: # 자연수일 때
        heapq.heappush(h, num) # 힙 리스트에 해당 숫자 push