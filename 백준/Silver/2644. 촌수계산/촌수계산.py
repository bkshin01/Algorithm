from collections import deque
import sys
input = sys.stdin.readline

def DFS(start, target, chon, visited):
    chon += 1
    visited.append(start)

    if target in graph[start]:
        print(chon)
        exit()

    for node in graph[start]:
        if node not in visited:
            DFS(node, target, chon, visited)

n = int(input())
ta, tb = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []

DFS(ta, tb, 0, [])
print(-1)