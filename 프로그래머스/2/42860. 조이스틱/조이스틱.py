def solution(name):
    n = len(name)
    
    # 상하 이동
    ud_move = 0
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in name:
        ud_move += min(dic.index(ch), len(dic)-dic.index(ch))
    
    # 좌우 이동
    lr_move = n - 1
    for i in range(n):
        next = i + 1
        while next < n and name[next] == "A":
            next += 1
        lr_move = min(lr_move, 2*i+(n-next), i+2*(n-next))
        
    return ud_move + lr_move