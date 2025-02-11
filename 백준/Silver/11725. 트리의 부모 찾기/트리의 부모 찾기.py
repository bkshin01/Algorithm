import sys
input = sys.stdin.readline
MAX = 10 ** 5

def DFS(n):
    stack = [n]
    parent = [0] * (MAX+1)
    while stack:
        curr = stack.pop()

        for next in graph[curr]:
            if not parent[next]:
                parent[next] = curr
                stack.append(next)
    return parent

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*DFS(1)[2:n+1], sep="\n")