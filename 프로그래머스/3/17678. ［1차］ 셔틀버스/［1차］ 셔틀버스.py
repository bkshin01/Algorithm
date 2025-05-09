def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def to_hhmm(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    crew = sorted([to_minutes(time) for time in timetable])
    bus_time = 9 * 60

    for i in range(n):
        count = 0
        while crew and crew[0] <= bus_time and count < m:
            last_person = crew.pop(0)
            count += 1
        bus_time += t
    
    last_bus = 9 * 60 + (n - 1) * t
    if count < m:
        return to_hhmm(last_bus)
    else:
        return to_hhmm(last_person - 1)