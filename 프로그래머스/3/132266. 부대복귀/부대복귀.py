from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    q = deque([destination])
    visited[destination] = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    
    return [visited[i] for i in sources]