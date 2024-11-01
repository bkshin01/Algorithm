def solution(nums):
    length = len(set(nums))
    if length <= len(nums)/2:
        return length
    return len(nums)/2