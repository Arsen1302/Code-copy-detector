class Solution:
	def solution_1239_5(self, nums: List[int]) -> int:
		negative = 1
		for number in nums:
			if number == 0:
				return 0
			elif number < 0:
				negative *= -1
		return negative