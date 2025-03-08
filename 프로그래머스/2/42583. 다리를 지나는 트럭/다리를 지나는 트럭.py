from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    time = 0
    q_sum = 0
    bridge = deque([0]*(bridge_length))
    
    while bridge:
        time += 1
        q_sum -= bridge.popleft()
        
        if truck_weights:
            if q_sum+truck_weights[0] <= weight:
                front = truck_weights.pop(0)
                bridge.append(front)
                q_sum += front
            else:
                bridge.append(0)
                
    return time