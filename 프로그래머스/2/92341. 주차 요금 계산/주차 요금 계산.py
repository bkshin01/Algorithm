from math import ceil

def solution(fees, records):
    parking_lot = {} # 차량번호 : 입차시각
    car_time = {} # 차량번호 : 주차시간
    
    for r in records:
        time, car_num, direction = r.split()
        if direction == 'IN':
            parking_lot[car_num] = time
        else:
            in_time = parking_lot.pop(car_num)
            h1, m1 = map(int, in_time.split(":"))
            h2, m2 = map(int, time.split(":"))
            total = (h2 * 60 + m2) - (h1 * 60 + m1)
            car_time[car_num] = car_time.get(car_num, 0) + total
            
            
    if parking_lot: # 남은 차들 처리 (23:59)
        out_time = '23:59'
        for car_num, in_time in parking_lot.items():
            h1, m1 = map(int, in_time.split(":"))
            total = (23*60+59) - (h1*60+m1)
            car_time[car_num] = car_time.get(car_num, 0) + total
    
    result = {}
    for car, time in car_time.items():
        if time <= fees[0]:
            fee = fees[1]
        else:
            extra = time - fees[0]
            fee = fees[1] + ceil(extra/fees[2]) * fees[3]
        
        result[car] = fee
    
    return [fee for _, fee in sorted(result.items())]
            