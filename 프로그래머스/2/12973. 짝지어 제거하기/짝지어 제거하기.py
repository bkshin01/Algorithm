def solution(s):
    while True:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        if stack:
            return 0
        else:
            return 1