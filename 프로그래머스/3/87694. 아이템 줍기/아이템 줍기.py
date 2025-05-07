from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def solution(rectangle, characterX, characterY, itemX, itemY):
    # maps 초기화
    maps = [[-1 for _ in range(102)] for _ in range(102)]
    
    # maps 갱신
    for r in rectangle:
        a1, b1, a2, b2 = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for a in range(a1, a2+1):
            for b in range(b1, b2+1):
                if a1<a<a2 and b1<b<b2:
                    maps[a][b] = 1 # 내부
                elif maps[a][b] != 1:
                    maps[a][b] = 0 # 테두리
    
    # BFS 최단 거리 탐색
    q = deque([[characterX*2, characterY*2]])
    visited = [[1 for _ in range(102)] for _ in range(102)]
    
    while q:
        cx, cy = q.popleft()
        if cx == itemX*2 and cy == itemY*2:
            return visited[cx][cy] // 2
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if maps[nx][ny] == 0 and visited[nx][ny] == 1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
    
    return 0       