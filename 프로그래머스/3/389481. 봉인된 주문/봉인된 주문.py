def solution(n, bans):
    def spell2num(spell):
        result = 0
        for ch in spell:
            result *= 26
            result += (ord(ch) - ord("a") + 1)
        return result
    def num2spell(num):
        result = []
        while num:
            result.append(num%26 or 26)
            num //= 26
            num -= (result[-1] == 26)
        return "".join(map(lambda x:chr(x+ord("a")-1), result[::-1]))
    sorted_bans = sorted([spell2num(spell) for spell in bans])
    for ban in sorted_bans:
        if ban <= n:
            n += 1
        else:
            break
    return num2spell(n)
