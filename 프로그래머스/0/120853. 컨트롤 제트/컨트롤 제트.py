def solution(s):
    stack = []
    answer = 0
    string = s.split()
    for ch in string:
        if ch == "Z":
            answer -= stack.pop()
            stack = []
        else:
            answer += int(ch)
            stack.append(int(ch))
    return answer