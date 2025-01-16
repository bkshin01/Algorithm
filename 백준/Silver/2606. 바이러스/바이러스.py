n = int(input()) # 노드 개수
v = int(input()) # 간선 개수

# n을 고려해 그래프 준비
graph = [[] for i in range(n+1)]

# v을 고려해 그래프 채우기
for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b] # graph[n] = n에 연결된 노드의 값
    graph[b] += [a]

# dfs 정의
def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            for neighbor in graph[curr]:
                stack.append(neighbor)
    return visited
    
print(len(dfs(graph, 1)) - 1)