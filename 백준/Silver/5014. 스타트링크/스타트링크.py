from collections import deque
import sys
input = sys.stdin.readline


def BFS(start, target):
    queue = deque([start])
    visited = {start:0}

    while queue:
        curr = queue.popleft()
        if curr == target:
            return visited[target]
        for i in (curr+u, curr-d):
            if 1<=i<=f and i not in visited:
                visited[i] = visited[curr] + 1
                queue.append(i)
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
print(BFS(s, g))