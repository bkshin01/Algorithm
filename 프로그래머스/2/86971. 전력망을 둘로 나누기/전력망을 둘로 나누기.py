from collections import deque

def BFS(start, graph, visited):
    result = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        if not visited[cur]:
            visited[cur] = True
            result += 1
            for nxt in graph[cur]:
                if not visited[nxt]:
                    q.append(nxt)
    return result

def solution(n, wires):
    answer = 100
    for i in range(n-1):
        result = []
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        w = wires[:i] + wires[i+1:]
        
        for s, e in w:
            graph[s].append(e)
            graph[e].append(s)
        
        for j in range(1, n+1):
            if not visited[j]:
                result.append(BFS(j, graph, visited))
        
        answer = min(answer, max(result)-min(result))
    return answer