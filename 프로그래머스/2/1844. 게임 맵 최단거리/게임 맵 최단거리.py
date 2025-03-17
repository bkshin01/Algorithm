from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        cx, cy = queue.popleft()        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m or maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]