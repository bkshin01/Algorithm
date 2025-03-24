from itertools import permutations

def check(users, banned):
    for i in range(len(banned)):
        if len(users[i]) != len(banned[i]):
            return False

        for j in range(len(users[i])):
            if banned[i][j] == "*":
                continue
            if banned[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    all_permutations = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for per in all_permutations:
        if not check(per, banned_id):
            continue
        else:
            per = set(per)
            if per not in ban_set:
                ban_set.append(per)

    return len(ban_set)