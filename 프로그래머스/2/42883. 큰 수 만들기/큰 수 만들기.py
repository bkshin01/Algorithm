def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    while k:
        stack.pop()
        k -= 1

    return ''.join(stack)