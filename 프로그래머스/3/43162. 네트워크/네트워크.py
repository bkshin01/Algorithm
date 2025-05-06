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
    answer = 0
    connected = [False] * n
    for i in range(n):
        if not connected[i]:
            BFS(i, connected, computers)
            answer += 1
    return answer