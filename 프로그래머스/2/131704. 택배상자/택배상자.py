def solution(order):
    stack = []
    result = 0
    cur_idx = 0

    for i in range(len(order)):
        stack.append(i+1)
        while stack[-1] == order[cur_idx]:
            cur_idx += 1
            result += 1
            stack.pop()
            if len(stack) == 0:
                break
                
    return result