from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0 # 사각형 내부
                elif graph[i][j] != 0:
                    graph[i][j] = 1 # 테두리
    
    sx, sy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    visited = [[1 for _ in range(102)] for _ in range(102)]
    q = deque()
    q.append((sx, sy))
    while q:
        cx, cy = q.popleft()
        if cx == ix and cy == iy:
            return visited[cx][cy] // 2
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[cx][cy]
                q.append((nx, ny))
    return 0