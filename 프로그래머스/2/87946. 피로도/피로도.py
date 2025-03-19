def DFS(k, cnt, dungeons, visited):
    max_cnt = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            max_cnt = max(max_cnt, DFS(k - dungeons[i][1], cnt + 1, dungeons, visited))
            visited[i] = False
    return max_cnt

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    return DFS(k, 0, dungeons, visited)