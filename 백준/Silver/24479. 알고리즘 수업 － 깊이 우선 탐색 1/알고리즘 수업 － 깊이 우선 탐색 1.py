import sys
input = sys.stdin.readline

def DFS(start_node):
    stack = [start_node]
    visited = [0] * (n+1)
    result = [0] * (n+1)
    cnt = 1

    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = 1
            result[curr] = cnt
            cnt += 1
            for neighbor in graph[curr]:
                stack.append(neighbor)
    return result

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort(reverse=True)

# DEBUGGING
# print(graph)

answer = DFS(r)
print(*answer[1:], sep="\n")