def solution(s):
    result = 0
    for ch in s.lower():
        if ch == 'p':
            result += 1
        elif ch == 'y':
            result -= 1
            
    if result == 0:
        return True
    return False