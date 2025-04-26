def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        a = i // n
        b = i % n
        result.append(max([a, b])+1)
    return result