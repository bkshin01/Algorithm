def solution(sides):
    sorted_sides = sorted(sides, reverse=True)
    if sorted_sides[0] < (sorted_sides[1] + sorted_sides[2]):
        return 1
    return 2