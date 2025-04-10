def solution(babbling):
    dic = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        for can in dic:
            if can in b:
                b = b.replace(can, "*")
        if len(b) == b.count("*"):
            answer += 1
    return answer