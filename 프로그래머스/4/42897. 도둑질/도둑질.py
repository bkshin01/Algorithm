def solution(money):
    if len(money) == 1:
        return money[0]
    
    n = len(money)
    dp1 = [0] + money[:-1] # 1번을 선택하는 dp (범위: 1 ~ n-1)
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
    
    dp2 = [0] + money[1:] # 1번을 선택하지 않는 dp (범위: 2 ~ n)
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])

    return max(dp1[-1], dp2[-1])