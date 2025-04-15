def solution(brown, yellow):
    candidates = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            candidates.append((i, yellow//i))
    for a, b in candidates:
        if brown == (a+b)*2+4:
            return sorted([a+2, b+2], reverse=True)