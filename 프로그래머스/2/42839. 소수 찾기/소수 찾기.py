from itertools import permutations

def isPrime(num):
    if(num <= 1):
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
    
def solution(numbers):
    arr = list(numbers)
    allNums = set()
    for i in range(1, len(numbers)+1):
        permutationList = permutations(arr, i)
        for perm in permutationList:
            num = int(''.join(perm))
            allNums.add(num)

    count = 0
    for num in allNums:
        if isPrime(num):
            count+=1
    return count