import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(node):
    for i in graph[node]: # node와 연결된 모든 노드 중에서
        if parent[i] == 0: # 부모가 없다고 표시된 노드
            parent[i] = node # node를 부모로 표시
            DFS(i) # 다시 해당 노드에 대해 DFS

DFS(1)
for j in range(2, len(parent)):
    print(parent[j])