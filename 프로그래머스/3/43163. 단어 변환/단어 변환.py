from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    def check(str1, str2):
        cnt = 0
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                cnt += 1
        if cnt == 1:
            return True
        return False
    
    q = deque()
    q.append((begin, 0))
    visited = {begin : True}
    
    while q:
        cur_word, cur_cnt = q.popleft()
        if cur_word == target:
            return cur_cnt
        for nxt in (w for w in words if check(w, cur_word)):
            if nxt not in visited:
                visited[nxt] = True
                q.append((nxt, cur_cnt+1))