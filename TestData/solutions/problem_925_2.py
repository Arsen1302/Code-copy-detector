class Solution:
	def solution_925_2(self, nums: List[int], index: List[int]) -> List[int]:
		target = []

		for num, idx in zip(nums, index):
			target.insert(idx, num)

		return target