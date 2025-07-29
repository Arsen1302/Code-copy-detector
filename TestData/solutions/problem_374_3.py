class Solution:
	def solution_374_3(self, pairs: List[List[int]]) -> int:
		pairs = sorted(pairs)
		arr = [1] * len(pairs)

		for i in range(1,len(pairs)):
			subprob = [arr[k] for k in range(i) if pairs[k][1] < pairs[i][0]]
			arr[i] = max(subprob, default=0) + 1

		return max(arr)