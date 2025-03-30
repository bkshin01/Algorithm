def solution(my_string):
    answer = 0
    idx = 0
    tmp = ''
    while idx < len(my_string):
        if my_string[idx].isdigit():
            tmp += my_string[idx]
        elif not my_string[idx].isdigit() and tmp != '':
            answer += int(tmp)
            tmp = ''
        idx += 1
    if tmp != '':
        answer += int(tmp)
    return answer