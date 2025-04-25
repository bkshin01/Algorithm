def solution(sequence):
    answer = -float('inf')
    psum1, psum2 = 0, 0
    min1, min2 = 0, 0
    pulse = 1
    
    for num in sequence:
        psum1 += num * pulse
        psum2 += num * -pulse
        
        answer = max(answer, psum1-min1, psum2-min2)
        
        # 이전까지의 합을 선택 or 지금 숫자부터 다시 시작
        min1 = min(min1, psum1)
        min2 = min(min2, psum2)
        
        pulse *= -1
    
    return answer