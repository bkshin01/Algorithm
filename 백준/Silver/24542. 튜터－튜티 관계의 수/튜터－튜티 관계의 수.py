from collections import deque
import sys
input = sys.stdin.readline
MOD = 1000000007

def bfs(node):
    queue = deque([node])
    visited[node] = True
    cnt = 1
    while queue:
        cur = queue.popleft()
        for next in arr[cur]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = True
            cnt += 1
    return cnt

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False for _ in range(n+1)]
answer = 1

for node in range(1, n+1):
    if not visited[node]:
        size = bfs(node)
        answer *= size
        answer %= MOD

print(answer)