from heapq import heappop, heappush

def solution(operations):
    min_heap = []
    max_heap = []
    
    for oper in operations:
        op, num = oper.split()
        if op == "I":
            heappush(min_heap, int(num))
            heappush(max_heap, -1*int(num))
        elif num == "1" and max_heap:
            min_heap.remove(-1*heappop(max_heap))
        elif num == "-1" and min_heap:
            max_heap.remove(-1*heappop(min_heap))
            
    if max_heap and min_heap:
        return [-1*heappop(max_heap), heappop(min_heap)]
    else:
        return [0, 0]