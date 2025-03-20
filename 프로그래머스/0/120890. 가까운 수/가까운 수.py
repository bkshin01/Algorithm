def solution(array, n):
    answer = 100
    diff_arr = []
    for num in array:
        if num == n:
            return n
        elif num > n:
            diff_arr.append(num-n)
        else:
            diff_arr.append(n-num)
    
    m = min(diff_arr)
    for i, num in enumerate(diff_arr):
        if num == m and answer > array[i]:
            answer = array[i]
            
    return answer