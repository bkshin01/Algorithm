import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for i in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DEBUGGING
# print(graph)

stack = [1]
while stack:
    curr = stack.pop()
    for i in graph[curr]:
        if parent[i] == 0:
            parent[i] = curr
            stack.append(i)

for j in range(2, n+1):
    print(parent[j])