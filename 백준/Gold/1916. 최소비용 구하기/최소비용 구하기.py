from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(graph, start, end):
    distance = [float("inf")] * (len(graph))
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        cur_price, cur_node = heappop(queue)
        if distance[cur_node] < cur_price:
            continue
        for ee, pp in graph[cur_node]:
            cost = distance[cur_node] + pp
            if cost < distance[ee]:
                distance[ee] = cost
                heappush(queue, (cost, ee))
    # DEBUGGING
    # print(distance)
    return distance[end]

n=int(input())
m=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))
start, end = map(int, input().split())

# DEBUGGING
# print(graph)

print(dijkstra(graph, start, end))