from itertools import permutations

def prime_check(num):
    if(num <= 1):
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    arr = list(numbers)
    nums = set()
    for i in range(1, len(numbers)+1):
        p_list = permutations(arr, i)
        for p in p_list:
            num = int(''.join(p))
            nums.add(num)

    count = 0
    for num in nums:
        if prime_check(num):
            count+=1
    return count