from heapq import heappush, heappop

def solution(operations):
    Mq = []
    mq = []
    for operation in operations:
        op, n = operation.split()
        if op == "I":
            heappush(Mq, -int(n))
            heappush(mq, int(n))
        elif n == "1":
            if Mq:
                tmp = heappop(Mq)
                mq.remove(-1*tmp)
        elif n == "-1":
            if mq:
                tmp = heappop(mq)
                Mq.remove(-1*tmp)
    answer = [0, 0]
    if mq:
        answer[0] = -1*heappop(Mq)
        answer[1] = heappop(mq)
    
    return answer