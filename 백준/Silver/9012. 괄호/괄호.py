# 입력 데이터들을 리스트로 저장
T = int(input())
target_list = []
while T:
    target_list.append(input())
    T -= 1

# 판별
for target in target_list: # 저장한 문자열 각각에 대하여
    stack = []
    for i in target: # 문자열의 각 문자에 대하여
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: # break하지 않은 경우
        if not stack:
            print("YES")
        else:
            print("NO")