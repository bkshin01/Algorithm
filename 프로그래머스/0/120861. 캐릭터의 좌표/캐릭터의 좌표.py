def solution(keyinput, board):
    dic = {'left':[-1, 0],
          'right':[1,0],
          'up':[0, 1],
          'down':[0, -1],}
    cur = [0, 0]
    w = int(board[0]//2)
    h = int(board[1]//2)
    for k in keyinput:
        x = cur[0] + dic[k][0]
        if -w <= x <= w:
            cur[0] = x
        y = cur[1] + dic[k][1]
        if -h <= y <= h:
            cur[1] = y
    return cur