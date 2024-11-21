def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    for i, ans in enumerate(answers):
        if ans == stu1[i%len(stu1)]:
            score[0] += 1
        if ans == stu2[i%len(stu2)]:
            score[1] += 1
        if ans == stu3[i%len(stu3)]:
            score[2] += 1
    
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)
            
    return result