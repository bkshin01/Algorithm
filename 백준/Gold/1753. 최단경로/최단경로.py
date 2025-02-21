from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(graph, start):
    distance = [float("INF")] * (len(graph))
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        cur_dist, cur_node = heappop(queue)
        if distance[cur_node] < cur_dist:
            continue
        for vv, ww in graph[cur_node]:
            cost = distance[cur_node] + ww
            if cost < distance[vv]:
                distance[vv] = cost
                heappush(queue, (cost, vv))
    return distance

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# DEBUGGING
# for i in graph:
#     print(i)

result = dijkstra(graph, k)

# DEBUGGING
# print(result)

for i in result[1:]:
    if i == float("inf"):
        print("INF")
    else:
        print(i)