def solution(clothes):
    dict = {}
    for c in clothes:
        if c[1] in dict:
            dict[c[1]].append(c[0])
        else:
            dict[c[1]] = [None, c[0]]
    answer = 1
    for key, values in dict.items():
        answer *= len(values)

    return answer - 1