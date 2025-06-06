def solution(N, number):
    if N == number:
        return 1
    
    # dp[i] = i개의 N으로 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].update([a+b, a-b, a*b])
                    if b != 0:
                        dp[i].add(a//b)
        
        if number in dp[i]:
            return i
        
    return -1