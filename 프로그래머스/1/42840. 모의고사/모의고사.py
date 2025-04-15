def solution(answers):
    n = len(answers)
    result = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]*(n//5) + [1, 2, 3, 4, 5][:n%5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]*(n//8) + [2, 1, 2, 3, 2, 4, 2, 5][:n%8]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(n//10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:n%10]
    
    for i in range(n):
        a = answers[i]
        if a == s1[i]:
            result[0] += 1
        if a == s2[i]:
            result[1] += 1
        if a == s3[i]:
            result[2] += 1
    
    answer = []
    for i in range(3):
        r = result[i]
        if r == max(result):
            answer.append(i+1)
    return answer