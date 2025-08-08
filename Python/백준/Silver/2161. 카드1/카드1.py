from collections import deque

n = int(input())
stack = deque([i for i in range(1, n+1)])
result = []

while stack:
    result.append(stack.popleft())
    if stack:
        stack.append(stack.popleft())

print(*result)