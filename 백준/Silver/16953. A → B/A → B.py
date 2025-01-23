from collections import deque

def BFS(start, target):
    queue = deque([start])
    visited = {start:0}

    while queue:
        curr = queue.popleft()
        if curr == target:
            return visited[target] + 1
        for i in (curr*2, curr*10+1):
            if 1 <= i <= target and i not in visited:
                visited[i] = visited[curr] + 1
                queue.append(i)
    return -1

a, b = map(int, input().split())
print(BFS(a, b))