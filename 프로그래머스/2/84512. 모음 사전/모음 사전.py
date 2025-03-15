def solution(word):
    answer = 0
    dict = []
    vowel = 'AEIOU'
    
    def dfs(length, w):
        if length == 5:
            return
        for i in range(len(vowel)):
            dict.append(w + vowel[i])
            dfs(length + 1, w + vowel[i])
    dfs(0, '')
    return dict.index(word) + 1