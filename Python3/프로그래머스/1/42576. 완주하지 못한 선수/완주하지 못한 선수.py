import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]   # 완주하지 못한 선수는 단 한명으므로 [0] 사용