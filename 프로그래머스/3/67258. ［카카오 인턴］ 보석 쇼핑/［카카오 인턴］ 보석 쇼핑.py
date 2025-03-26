def solution(gems):
    n = len(gems)
    answer = [0, n]
    all_gems = len(set(gems))
    l, r = 0, 0
    dic = {gems[0]:1}
    
    while l<n and r<n:
        if len(dic) == all_gems:
            if r-l < answer[1]-answer[0]:
                answer = [l, r]
            else:
                dic[gems[l]] -= 1
                if dic[gems[l]] == 0:
                    del dic[gems[l]]
                l += 1
        else:
            r += 1
            if r == n:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1
            
    return [answer[0]+1, answer[1]+1]