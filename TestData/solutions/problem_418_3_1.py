class Solution:
	def solution_418_3_1(self, nums: List[int], target: int) -> int:

		def solution_418_3_2(array, start, end, target):

			if start <= end:

				mid = (start + end)//2

				if array[mid] == target:
					return mid

				elif array[mid] < target:
					start = mid + 1

				if array[mid] > target:
					end = mid - 1

				return solution_418_3_2(nums, start, end, target)

			return -1

		start = 0
		end = len(nums)-1

		result = solution_418_3_2(nums, start, end, target) 

		return result