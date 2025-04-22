def solution(sequence):
    max_sum = -float('inf')
    alt_sum1 = alt_sum2 = 0
    min1 = min2 = 0
    pulse = 1
    
    for num in sequence:
        alt_sum1 += num * pulse
        alt_sum2 += num * -pulse
        
        max_sum = max(max_sum, alt_sum1-min1, alt_sum2-min2)
        
        min1 = min(min1, alt_sum1)
        min2 = min(min2, alt_sum2)
        
        pulse *= -1
    
    return max_sum