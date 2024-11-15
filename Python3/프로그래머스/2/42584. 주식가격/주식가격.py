from collections import deque

def solution(prices):
    # prices의 모든 p에 대해서 다음을 반복:
        # 초를 세면서 prices 내에 p보다 더 작은 값이 있는지 확인
            # 있으면 sec를 기록하고 break
            
    queue = deque(prices)
    answer = []
    
    while queue:
        t = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if t > q:
                break
        answer.append(sec)
    return answer