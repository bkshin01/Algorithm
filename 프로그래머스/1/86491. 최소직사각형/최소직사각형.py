def solution(sizes):
    w, h = [], []
    for size in sizes:
        a, b = size[0], size[1]
        if a > b:
            w.append(a)
            h.append(b)
        else:
            w.append(b)
            h.append(a)
    return max(w)*max(h)