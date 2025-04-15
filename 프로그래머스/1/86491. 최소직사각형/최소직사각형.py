def solution(sizes):
    w, h = 0, 0
    for s in sizes:
        if max(s) > w:
            w = max(s)
        if min(s) > h:
            h = min(s)
    return w*h