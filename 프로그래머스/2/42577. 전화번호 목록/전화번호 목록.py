def solution(phone_book):
    dict = {}
    for i, number in enumerate(phone_book):
        dict[number] = i
        
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in dict:
                return False
    return True