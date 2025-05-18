def solution(numbers):
    n = len(numbers)
    stack = []
    result = [-1 for _ in range(n)]
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
    
    return result