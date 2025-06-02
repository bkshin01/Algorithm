from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def DFS(n, graph, start):
    stack = [start]
    visited = [False] * (n+1)
    result = []
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = True
            result.append(cur)
            for nxt in sorted(graph[cur], reverse=True):
                if not visited[nxt]:
                    stack.append(nxt)
    return result

def BFS(n, graph, start):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    result = []
    while q:
        cur = q.popleft()
        result.append(cur)
        for nxt in sorted(graph[cur]):
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return result

n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*DFS(n, graph, v))
print(*BFS(n, graph, v))