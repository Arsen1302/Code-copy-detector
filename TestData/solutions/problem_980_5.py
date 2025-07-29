class Solution:
	def solution_980_5(self, target: List[int], arr: List[int]) -> bool:
		dic1 = Counter(target)
		dic2 = Counter(arr)
		return dic1==dic2