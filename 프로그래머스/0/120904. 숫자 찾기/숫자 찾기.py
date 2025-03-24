def solution(num, k):
    for i, ch in enumerate(str(num)):
        if ch == str(k):
            return i+1
    return -1