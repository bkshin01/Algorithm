from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        front = q.popleft()
        time = 0
        for p in q:
            time += 1
            if front > p:
                break
        answer.append(time)
    return answer