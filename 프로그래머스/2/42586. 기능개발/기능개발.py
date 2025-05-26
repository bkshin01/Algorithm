def solution(progresses, speeds):
    result = []
    while progresses:
        n = len(progresses)
        for i in range(n):
            progresses[i] += speeds[i]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        if cnt > 0:
            result.append(cnt)
    
    return result