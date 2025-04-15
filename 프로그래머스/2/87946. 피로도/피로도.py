from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for perm in permutations(dungeons, len(dungeons)):
        cur = k
        cnt = 0
        for required, consumed in perm:
            if cur >= required:
                cur -= consumed
                cnt += 1
            else:
                break
        max_count = max(max_count, cnt)
    return max_count