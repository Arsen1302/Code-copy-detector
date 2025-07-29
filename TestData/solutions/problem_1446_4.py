class Solution:
	def solution_1446_4(self, nums: List[int]) -> int:
		prev, result = 1, 1

		for i in range(1,len(nums)):
			if nums[i] == nums[i-1]-1:
				result += prev + 1
				prev += 1

			else:
				result += 1
				prev = 1

		return result