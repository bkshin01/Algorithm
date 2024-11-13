def solution(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True