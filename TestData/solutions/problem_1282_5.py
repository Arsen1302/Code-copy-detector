class Solution:
	def solution_1282_5(self, servers: List[int], tasks: List[int]) -> List[int]:

		ans = []
		freeServers = []
		usedServers = []

		# push all available severs into free server heap, smallest server weight on top
		for idx, serverWeight in enumerate(servers):
			heapq.heappush(freeServers, (serverWeight, idx))

		# iterate through each task
		for idx, taskTime in enumerate(tasks):
			curTime = idx

			# while a servers completion time is less than or equal to curTime, pop it and add to free
			while usedServers and usedServers[0][0] <= curTime:
				_, w, i = heapq.heappop(usedServers)
				heapq.heappush(freeServers, (w, i))

			# if there is a free server, use it
			if freeServers:
				weight, i = heapq.heappop(freeServers)
				ans.append(i)

				taskCompletion = curTime + taskTime
				heapq.heappush(usedServers, (taskCompletion, weight, i))
			else:
				# if no free server, top most used server will be next free, so update completion time 
				tCompletion, weight, i = heapq.heappop(usedServers)
				tCompletion += taskTime

				heapq.heappush(usedServers, (tCompletion, weight, i))
				ans.append(i)

		return ans