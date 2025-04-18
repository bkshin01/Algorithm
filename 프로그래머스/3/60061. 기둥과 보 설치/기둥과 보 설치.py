def available(structures):
    for x, y, a in structures:
        if a == 0: # 기둥
            if y == 0 or (x, y-1, 0) in structures or (x-1, y, 1) in structures or (x, y, 1) in structures:
                continue
            return False
        elif a == 1: # 보
            if (x, y-1, 0) in structures or (x+1, y-1, 0) in structures or ((x-1, y, 1) in structures and (x+1, y, 1) in structures):
                continue
            return False
    return True

def solution(n, build_frame):
    structures = set()
    
    for x, y, a, b in build_frame: # 기둥0, 설치1
        if b == 1: # 설치
            structures.add((x, y, a))
            if not available(structures):
                structures.remove((x, y, a))
        elif b == 0: # 삭제
            structures.remove((x, y, a))
            if not available(structures):
                structures.add((x, y, a))
    
    return sorted(structures, key=lambda x: (x[0], x[1], x[2]))