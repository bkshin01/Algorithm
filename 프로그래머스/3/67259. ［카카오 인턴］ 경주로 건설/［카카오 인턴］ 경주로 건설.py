from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]    
def solution(board):
    n = len(board)
    def BFS(start_direction):
        visited = [[float('inf')] * n for _ in range(n)]
        visited[0][0] = 0
        q = deque()
        q.append([0, 0, 0, start_direction])
        while q:
            cx, cy, cc, cd = q.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if board[nx][ny] == 1:
                    continue
                else:
                    if i == cd:
                        nc = cc + 100
                    else:
                        nc = cc + 600
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i])
                
        return visited[-1][-1]

    return min([BFS(0), BFS(2)])