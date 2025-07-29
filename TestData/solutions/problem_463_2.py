class Solution:
	def solution_463_2(self, arr: List[int]) -> int:
		temp_sum, block = 0, 0
		for i in range(len(arr)):
			temp_sum += arr[i] - i
			if temp_sum == 0:
				block += 1
		return block