def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slice = array[commands[i][0]-1:commands[i][1]]
        slice.sort()
        answer.append(slice[commands[i][2]-1])
    return answer