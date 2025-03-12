from collections import deque

def bfs(start, graph, visited):
    cnt = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        if not visited[cur]:
            visited[cur] = True
            cnt += 1
            for node in graph[cur]:
                if not visited[node]:
                    q.append(node)
    return cnt

def solution(n, wires):
    answer = 100
    for i in range(n-1):
        result = []
        graph = [[] for _ in range(n+1)]
        visited = [False] * (len(graph)+1)
        w = wires[:i]+wires[i+1:]
        
        for wire in w:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
            
        for j in range(n+1):
            if not visited[j]:
                result.append(bfs(j, graph, visited))
        
        if result[2] > result[1]:
            tmp = result[2]-result[1]
        else:
            tmp = result[1]-result[2]
        
        if tmp < answer:
            answer = tmp
        
    return answer