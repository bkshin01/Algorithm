def solution(A, B):
    if A == B:
        return 0
    for i in range(len(A)):
        tmp = A[-1]+A[:-1]
        if tmp == B:
            return i+1
        A = tmp
    return -1