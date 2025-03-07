def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        n = len(progresses)
        for i in range(n):
            progresses[i] += speeds[i]
        
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
    return answer