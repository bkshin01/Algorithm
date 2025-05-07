from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    result = 0
    while people:
        cur = people.pop()
        if people and people[0] + cur <= limit:
            people.popleft()
        result += 1
    return result