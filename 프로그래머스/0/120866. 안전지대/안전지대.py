def solution(board):
    # 역으로 주변에 지뢰가 없으면 안전지대로 count
    answer = 0
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    n = len(board)
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                tmp = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if board[nx][ny] == 1:
                        tmp += 1
                if tmp == 0:
                    answer += 1
    return answer