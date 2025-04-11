def solution(A, B):
    n = len(A)
    cnt = 0
    while True:
        if A == B:
            return cnt
        elif cnt >= n:
            return -1
        A = A[-1] + A[:n-1]
        cnt += 1