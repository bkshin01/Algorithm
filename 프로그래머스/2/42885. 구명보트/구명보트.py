def solution(people, limit):
    people.sort()
    l, r = 0, len(people)-1
    result = 0
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        result += 1
    
    return result