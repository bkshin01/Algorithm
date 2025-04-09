def solution(ineq, eq, n, m):
    oper = ineq
    if eq == '=':
        oper += '='
    if len(oper) == 1 and oper == '>' and n>m:
        return 1
    elif len(oper) == 1 and oper == '<' and n<m:
        return 1
    elif len(oper) == 2 and oper == '>=' and n>=m:
        return 1
    elif len(oper) == 2 and oper == '<=' and n<=m:
        return 1
    else:
        return 0