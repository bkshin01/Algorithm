def solution(id_pw, db):
    dic = {}
    for i, pw in db:
        dic[i] = pw
    if id_pw[0] in dic and id_pw[1] == dic[id_pw[0]]:
        return 'login'
    elif id_pw[0] in dic:
        return 'wrong pw'
    return 'fail'