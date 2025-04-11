def solution(M, N):
    answer = M - 1
    tmp = answer + 1
    answer += (N-1)*(tmp)
    return answer