class Solution:
	def solution_915_3(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

		graph = defaultdict(list)
		for e,m in enumerate(manager):
			graph[m].append(e)

		q = [[headID,0]]
		res = 0
		while q:
			newq = []
			local = 0
			for m,t in q:
				res = max(res,t)
				for e in graph[m]:
					newq.append([e,t+informTime[m]])

			q = newq[::]

		return res