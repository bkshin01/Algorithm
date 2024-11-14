from collections import deque

def solution(priorities, location):
    # 자료구조 하나에 다 집어넣고
    # 하나 뽑아서 자료구조의 다른 애들과 비교.
        # 나보다 더 큰애가 있으면 다시 넣기
            # 자료구조 내의 다른 애들과 모두 비교해봐야 함
        # 없으면 넘어가고 다음으로 반복
    # return할 값을 구하기 위해 인덱스 필요
    answer = 0
    queue = [(i, v) for i, v in enumerate(priorities)]
    
    while True:
        tmp = queue.pop(0)
        if any(tmp[1] < p[1] for p in queue):
            queue.append(tmp)
        else:
            answer += 1
            if tmp[0] == location:
                return answer