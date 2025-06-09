def solution(name):
    n = len(name)
    ud_move = 0
    
    for ch in name:
        diff = ord(ch) - ord('A')
        ud_move += min(diff, 26 - diff)
    
    lr_move = n - 1
    for i in range(n):
        nxt = i + 1
        while nxt < n and name[nxt] == 'A':
            nxt += 1
        lr_move = min(lr_move, 2*i+(n-nxt), i+2*(n-nxt))
    
    return ud_move + lr_move