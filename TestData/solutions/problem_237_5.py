class Solution:
	def solution_237_5(self, intervals: List[List[int]]) -> int:
		# greedy 
		# always pick the earlist end time because it provide more capacity to the later intervals
		intervals.sort(key = lambda x : x[1])
		# use fit to record the order or fitting intervals and compare with the next one
		# to check if the next one is fit
		fit = []
		for i in intervals:
			if fit == [] or i[0]>= fit[-1][1]:
				fit.append(i)

		return len(intervals) - len(fit)
		# time complexity: sorting (nlogn) + traversal (n) which is 0(nlogn)
		# space : the lenth of fit which is O(n)