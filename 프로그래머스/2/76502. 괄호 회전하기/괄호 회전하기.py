def check(string):
    stack = []
    for ch in string:
        if ch in ['[', '{', '(']:
            stack.append(ch)
        elif len(stack) == 0:
            return False
        else:
            tmp = stack[-1] + ch
            if tmp in ['[]', '{}', '()']:
                stack.pop()
    
    if stack:
        return False
    
    return True
            
            
def solution(s):
    n = len(s)
    if n % 2 == 1:
        return 0
    
    result = 0
    for i in range(n):
        if check(s):
            result += 1
        s = s[1:] + s[0]
    return result