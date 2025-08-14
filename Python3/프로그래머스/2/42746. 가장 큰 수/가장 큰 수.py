def solution(numbers):
    numbers_str = [str(i) for i in numbers]
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers_str)))