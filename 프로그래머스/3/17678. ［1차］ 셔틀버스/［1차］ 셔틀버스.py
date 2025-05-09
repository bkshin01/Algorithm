def to_minutes(string):
		h, m = map(int, string.split(":"))
		return h * 60 + m

def to_hhmm(minutes):
		h = minutes // 60
		m = minutes % 60
		return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
		crew = sorted([to_minutes(time) for time in timetable], reverse=True)
		bus_time = 9 * 60
		
		for i in range(n):
				cnt = 0
				while crew and crew[-1] <= bus_time and cnt < m:
						last_person = crew.pop()
						cnt += 1
				bus_time += t
		
		last_bus = 9 * 60 + (n-1) * t
		if cnt < m:
				return to_hhmm(last_bus)
		return to_hhmm(last_person - 1)