def solution(word):
    answer = 0
    dict = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            dict.append(w + words[i])
            dfs(cnt + 1, w + words[i])
    dfs(0, '')
    return dict.index(word) + 1