from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    time = 0
    cur_sum = 0
    bridge = deque([0] * bridge_length)
    
    while bridge:
        time += 1
        cur_sum -= bridge.popleft()
        
        if truck_weights:
            if cur_sum + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
                cur_sum += t
            else:
                bridge.append(0)
    
    return time