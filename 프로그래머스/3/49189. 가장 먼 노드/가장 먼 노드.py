from collections import deque

def BFS(graph, n):
    queue = deque([1])
    distance = {}
    distance[1] = 1
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if nxt not in distance:
                distance[nxt] = distance[cur] + 1
                queue.append(nxt)
    return distance

def solution(n, edge):
    distance = {}
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    dist = BFS(graph, n)
    Max = max(dist.values())
    answer = 0
    for k, v in dist.items():
        if v == Max:
            answer += 1
    return answer