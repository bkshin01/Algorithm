def solution(numbers):
    arr = []
    answer = ""
    
    for num in numbers:
        arr.append(str(num))
    arr.sort(key=lambda x: x*3, reverse=True)
    
    for a in arr:
        answer += a
    return str(int(answer))