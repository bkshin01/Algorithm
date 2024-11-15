from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼의 deque를 준비
    # 다리에 트럭이 있는 동안 반복문
        # 시간, 현재 다리 위의 트럭 무게 업데이트
        # 올려야 할 트럭이 남아있는 경우
            # 무게 조건을 만족하면
                # 다리에 트럭을 올리고, 현재 다리 위의 트럭 무게 업데이트
            # 만족하지 못하는 경우
                # 다리에 0을 올린다
    
    cnt = 0
    sec = 0
    cur_weight = 0
    bridge = deque([0]*bridge_length)
    
    while bridge:
        sec += 1
        cur_weight -= bridge.popleft()
        
        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
                cur_weight += t
            else:
                bridge.append(0)
    return sec