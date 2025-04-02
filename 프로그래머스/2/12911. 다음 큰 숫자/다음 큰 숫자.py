def solution(n):
    for i in range(n+1, n*2):
        if bin(i)[2:].count('1') == bin(n)[2:].count('1'):
            return i