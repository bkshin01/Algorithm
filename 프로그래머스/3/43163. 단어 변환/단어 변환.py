from collections import deque

def check(word_1, word_2):
    cnt = 0
    for a, b in zip(word_1, word_2):
        if a != b:
            cnt += 1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = {}
    q = deque([begin])
    visited[begin] = 0

    while q:
        cur = q.popleft()
        if cur == target:
            return visited[target]
        for nxt in [w for w in words if check(cur, w)]:
            if nxt not in visited:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1