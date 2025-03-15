answer = 0

def DFS(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            DFS(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    DFS(k, 0, dungeons, visited)
    return answer