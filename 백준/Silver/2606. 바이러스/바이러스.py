import sys
input = sys.stdin.readline

def DFS(start):
    stack = [start]
    visited = []

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            for neighbor in graph[curr][::-1]:
                stack.append(neighbor)
    return len(visited)

n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(DFS(1)-1)