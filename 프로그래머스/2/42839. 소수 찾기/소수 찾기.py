from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    all_set = set()
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers, i)
        for p in perm:
            num = int(''.join(p))
            all_set.add(num)
    
    answer = 0
    for n in all_set:
        if is_prime(n):
            answer += 1
    return answer