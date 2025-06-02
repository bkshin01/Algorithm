from collections import deque

def BFS(start, visited, graph):
    q = deque([start])
    while q:
        cur = q.popleft()
        visited[cur] = True
        for nxt, con in enumerate(graph[cur]):
            if nxt != cur and con == 1 and not visited[nxt]:
                q.append(nxt)

def solution(n, computers):
    result = 0
    connected = [False] * n
    for i in range(n):
        if not connected[i]:
            BFS(i, connected, computers)
            result += 1
    return result