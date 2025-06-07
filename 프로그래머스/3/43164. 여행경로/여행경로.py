def solution(tickets):
    graph = {}
    for a, b in tickets:
        graph[a] = graph.get(a, []) + [b]
        
    for v in graph.values():
        v.sort(reverse=True)
    
    result = []
    stack = ['ICN']
    
    while stack:
        top = stack[-1]
        
        if top not in graph or len(graph[top]) == 0:
            result.append(stack.pop())
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]
            
    return result[::-1]