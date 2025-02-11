from collections import deque

def BFS(f, s, g, u, d):
    queue = deque([s])
    visited = {s:0}
    while queue:
        curr = queue.popleft()
        if curr == g:
            return visited[g]
        for i in (curr+u, curr-d):
            if 1<=i<=f and i not in visited:
                visited[i] = visited[curr] + 1
                queue.append(i)
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
print(BFS(f, s, g, u, d))