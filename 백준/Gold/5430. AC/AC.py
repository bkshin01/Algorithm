from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input()
    n = int(input())
    arr_input = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_input[1:-1].split(',')))
    
    reverse = False
    error = False

    for oper in p:
        if oper == 'R':
            reverse = not reverse
        elif oper == 'D':
            if not arr:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()
    
    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")