def solution(answers):
    n = len(answers)
    s1 = [1, 2, 3, 4, 5]
    s1 = s1*(n//5) + s1[:(n%5)]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s2 = s2*(n//8) + s2[:(n%8)]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s3 = s3*(n//10) + s3[:(n%10)]
    result = [0]*(4)
    
    for i in range(n):
        if answers[i] == s1[i]:
            result[1]+=1
        if answers[i] == s2[i]:
            result[2]+=1
        if answers[i] == s3[i]:
            result[3]+=1
    
    answer = []
    for i in range(1, 4):
        if result[i] == max(result):
            answer.append(i)
    
    return answer