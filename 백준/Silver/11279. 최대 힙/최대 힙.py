from heapq import heappop, heappush
import sys
input = sys.stdin.readline

max_heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0 and max_heap:
        print(-1 * heappop(max_heap))
    elif x == 0:
        print(0)
    else:
        heappush(max_heap, -1 * x)