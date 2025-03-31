def solution(n):
    result = 1
    while n:
        if result%3 != 0 and '3' not in str(result):
            n -= 1
        result += 1
    return result - 1
    