from heapq import heappop, heappush

def solution(jobs):
		result = 0
		curtime = 0
		cnt = 0
		start = -1
		heap = []
		n = len(jobs)
	
		while cnt < n:
				for j in jobs:
						if start < j[0] <= curtime:
								heappush(heap, [j[1], j[0]])
				if heap:
						tmp = heappop(heap)
						start = curtime
						curtime += tmp[0]
						result += (curtime-tmp[1])
						cnt += 1
				else:
						curtime += 1
		
		return result // n