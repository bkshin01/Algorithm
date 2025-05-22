from collections import Counter

def solution(topping):
    result = 0
    A_counter = Counter(topping)
    A_cnt = len(A_counter)
    B_set = set()
    
    for t in topping:
        B_set.add(t)
        A_counter[t] -= 1
        if A_counter[t] == 0:
            A_cnt -= 1
        if len(B_set) == A_cnt:
            result += 1
    
    return result