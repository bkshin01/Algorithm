def solution(number, k):
    stack = []
    for num in number:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    while k:
        stack.pop()
        k -= 1
        
    return ''.join(stack)