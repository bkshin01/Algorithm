import sys
input = sys.stdin.readline

while True:
    str = input().rstrip()
    if str == ".":
        sys.exit()
    
    stack = []
    is_valid = True
    for ch in str:
        if ch == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif ch == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif ch in ['[', '(']:
            stack.append(ch)
        elif ch in [']', ')']:
            is_valid = False
            break

    if is_valid and not stack:
        print("yes")
    else:
        print("no")