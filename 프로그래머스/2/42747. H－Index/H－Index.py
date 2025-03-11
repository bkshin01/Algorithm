def solution(citations):
    citations.sort()
    answer = 0
    for i in range(1, citations[-1]):
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
        if cnt >= i and i > answer:
            answer = i
    return answer