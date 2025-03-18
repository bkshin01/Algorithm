def solution(tickets):
    graph = {}
    for de, ar in tickets:
        graph[de] = graph.get(de, []) + [ar]
    for i in graph:
        graph[i].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]
    return path[::-1]
            