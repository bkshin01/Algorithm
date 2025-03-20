def solution(my_string):
    answer = ''
    for ch in my_string:
        if ord(ch) >= ord('a'):
            answer += ch.upper()
        else:
            answer += ch.lower()
    return answer