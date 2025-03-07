def solution(s):
    stack = []
    for letter in s:
        if letter == "(":
            stack.append(1)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()
    if len(stack) > 0:
        return False
    return True