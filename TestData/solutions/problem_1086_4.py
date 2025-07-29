class Solution:
	def solution_1086_4(self, nums: List[int]) -> int:

		nums = sorted(nums)[::-1]

		for num in range(len(nums) + 1):

			count = 0

			for current_number in nums:

				if current_number >= num:

					count = count + 1

			if count == num:
				return num

		return -1