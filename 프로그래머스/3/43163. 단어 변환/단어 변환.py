from collections import deque

def BFS(start, target, words):
    q = deque()
    q.append((start, 0))
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            return cnt
        
        for w in words:
            tmp = 0
            for i, ch in enumerate(cur):
                if ch != w[i]:
                    tmp += 1
            if tmp == 1:
                q.append((w, cnt+1))
        
def solution(begin, target, words):
    if target not in words:
        return 0
    return BFS(begin, target, words)