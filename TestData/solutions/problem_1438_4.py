class Solution:
	def solution_1438_4(self, nums: List[int], time: int) -> List[int]:
		dpPrefix = [0] * len(nums)
		dpSuffix = [0] * len(nums)

		low, high = 1, len(nums)-2

		while low < len(nums):
			if nums[low-1] >= nums[low]:
				dpPrefix[low] += dpPrefix[low-1] + 1

			if nums[high] <= nums[high+1]:
				dpSuffix[low] += dpSuffix[low-1] + 1

			low += 1
			high -= 1

		result = []

		for i in range(len(nums)):
			if dpPrefix[i] >= time and dpSuffix[len(nums)-i-1] >= time:
				result.append(i)

		return result