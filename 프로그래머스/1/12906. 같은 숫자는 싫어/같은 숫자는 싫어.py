def solution(arr):
    s = []
    for num in arr:
        if len(s) == 0:
            s.append(num)
        else:
            top = s[-1]
            if top == num:
                continue
            else:
                s.append(num)
    return s
                