import sys
input = sys.stdin.readline

def DFS(node):
    visited[node] = 1
    neighbor = graph[node]
    if not visited[neighbor]:
        DFS(neighbor)

for _ in range(int(input())):
    cnt = 0
    n = int(input())
    visited = [0] * (n+1)
    graph = [0]
    graph += list(map(int, input().split()))
    
    # DEBUGGING
    # print(arr)
    
    for i in range(1, n+1):
        if not visited[i]:
            DFS(i)
            cnt += 1
    print(cnt)