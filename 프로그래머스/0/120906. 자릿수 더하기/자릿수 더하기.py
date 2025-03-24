def solution(n):
    answer = 0
    for ch in str(n):
        answer += int(ch)
    return answer