from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start, graph):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for vv, ww in graph[now]:
            cost = distance[now] + ww
            if cost < distance[vv]:
                distance[vv] = cost
                heappush(q, (cost, vv))
    return distance

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

answer = 0
for i in range(1, n+1):
    distance = dijkstra(i, arr)
    result = 0
    for j in range(1, n+1):
        if distance[j] <= m:
            result += item[j-1]
    if result > answer:
        answer = result

print(answer)