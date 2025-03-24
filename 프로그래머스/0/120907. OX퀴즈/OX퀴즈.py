def check(string):
    nums = []
    opers = ""
    print(string.split())
    for ch in string.split():
        if ch == "=":
            pass
        elif ch == "-" or ch == "+":
            opers += ch
        else:
            nums.append(int(ch))
    if opers == "-" and nums[0] - nums[1] == nums[2]:
        return True
    elif opers == "+" and nums[0] + nums[1] == nums[2]:
        return True
    else:
        return False

def solution(quiz):
    answer = []
    for q in quiz:
        if check(q):
            answer.append("O")
        else:
            answer.append("X")
    return answer