def solution(word):
    answer = 0
    dic = []
    vowel = 'AEIOU'
    
    def dfs(l, w):
        if l == 5:
            return
        for i in range(5):
            dic.append(w + vowel[i])
            dfs(l+1, w+vowel[i])
    
    dfs(0, '')
    return dic.index(word) + 1