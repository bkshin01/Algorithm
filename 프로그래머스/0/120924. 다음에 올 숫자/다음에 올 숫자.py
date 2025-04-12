def solution(common):
    # 등차수열인 경우
    diff = common[0] - common[1]
    for i in range(1, len(common)-1):
        if common[i]-common[i+1] == diff:
            continue
        else:
            #등비수열
            return common[-1]*(common[1]//common[0])
    return common[-1]-diff