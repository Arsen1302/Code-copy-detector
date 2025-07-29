class Solution:
	def solution_1655_2(self, nums: List[int]) -> bool:

		dictionary = {}

		for i in range(len(nums) - 1):

			subarray_sum = sum(nums[i:i+2])

			if subarray_sum not in dictionary:

				dictionary[subarray_sum] = nums[i:i+2]
			else:
				return True

		return False