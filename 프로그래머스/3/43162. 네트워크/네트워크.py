from collections import deque

def BFS(start, graph, visited):
    q = deque([start])
    while q:
        cur = q.popleft()
        visited[cur] = True
        for nxt, i in enumerate(graph[cur-1]):
            if i == 1 and (nxt+1) != cur and not visited[nxt+1]:
                q.append(nxt+1)
    
def solution(n, computers):
    answer = 0
    visited = [False] * (n+1)
    for com in range(1, n+1):
        if not visited[com]:
            answer += 1
            BFS(com, computers, visited)
    return answer