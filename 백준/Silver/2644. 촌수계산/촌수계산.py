import sys
input = sys.stdin.readline

def DFS(s, t):
    stack = [s]
    cnt = [-1] * (n+1)

    while stack:
        curr = stack.pop()
        if curr == t:
            return cnt[t]+1 # -1로 초기화되어 있었기 때문
        for neighbor in graph[curr]:
            if cnt[neighbor] == -1:
                cnt[neighbor] = cnt[curr] + 1
                stack.append(neighbor)
    return cnt[t]
        
n = int(input())
graph = [[] for _ in range(n+1)]
start, target = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(DFS(start, target))