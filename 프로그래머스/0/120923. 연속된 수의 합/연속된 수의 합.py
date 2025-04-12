def solution(num, total):
    answer = []
    s = 0
    for i in range(1, num):
        s += i
    start = (total-s) // num
    for i in range(start, start+num):
        answer.append(i)
    return answer