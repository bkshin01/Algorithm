def solution(numbers):
    result = set()
    for i in range(len(numbers)):
        for j in range(i):
            result.add(numbers[i]+numbers[j])
    return sorted(list(result))