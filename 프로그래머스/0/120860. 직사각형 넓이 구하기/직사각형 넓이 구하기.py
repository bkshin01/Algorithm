def solution(dots):
    xs = []
    ys = []
    for x, y in dots:
        xs.append(x)
        ys.append(y)
    return (max(xs)-min(xs))*(max(ys)-min(ys))