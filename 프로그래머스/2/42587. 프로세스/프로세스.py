def solution(priorities, location):
    q = []
    for i, p in enumerate(priorities):
        q.append((i, p))
    answer = 0
    while True:
        front = q.pop(0)
        if any(front[1] < i[1] for i in q):
            q.append(front)
        else:
            answer += 1
            if front[0] == location:
                return answer