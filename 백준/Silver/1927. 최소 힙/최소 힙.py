from heapq import heappush, heappop
import sys
input = sys.stdin.readline

min_heap = []
for _ in range(int(input())):
    num = int(input())
    if num == 0 and min_heap:
        print(heappop(min_heap))
    elif num == 0:
        print(0)
    else:
        heappush(min_heap, num)