def to_num(s):
    result = 0
    tmp = str(s).split('+')
    for t in tmp:
        result += int(t)
    return result

input_str = list(map(str, input().split('-')))
result = to_num(input_str[0])

for i in range(1, len(input_str)):
    result -= to_num(input_str[i])

print(result)