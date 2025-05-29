from heapq import heappush, heappop, heapify

def solution(scoville, K):
    result = 0
    heapify(scoville)
    front = heappop(scoville)
    while front < K:
        if len(scoville) == 0:
            return -1
        heappush(scoville, front + 2 * (heappop(scoville)))
        front = heappop(scoville)
        result += 1
    return result