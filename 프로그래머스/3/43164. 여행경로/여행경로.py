from collections import defaultdict

def DFS(node, graph, route):
    while graph[node]:
        nxt = graph[node].pop(0)
        DFS(nxt, graph, route)
    route.append(node)

def solution(tickets):
    graph = defaultdict(list)
    
    for de, ar in tickets:
        graph[de].append(ar)
    for key in graph:
        graph[key].sort()
    
    route = []
    DFS("ICN", graph, route)
    
    return route[::-1]