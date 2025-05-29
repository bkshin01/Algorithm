from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total_sum = 0
    total_num = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    
    while truck_weights:
        tmp = bridge.popleft()
        if tmp != 0:
            total_num -= 1
            total_sum -= tmp
            
        if truck_weights[0] + total_sum <= weight and total_num + 1 <= bridge_length:
            target = truck_weights.popleft()
            total_sum += target
            total_num += 1
            bridge.append(target)
        else:
            bridge.append(0)
            
        time += 1
        
    while total_num:
        tmp = bridge.popleft()
        if tmp != 0:
            total_num -= 1
        time += 1
    
    return time