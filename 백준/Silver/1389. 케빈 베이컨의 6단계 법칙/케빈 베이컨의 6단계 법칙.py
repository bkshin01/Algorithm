from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = visited[curr] + 1
                queue.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1):
    visited = [0] * (n + 1)
    BFS(i)
    result.append(sum(visited))

print(result.index(min(result))+1)