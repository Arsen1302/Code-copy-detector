class Solution:
	def solution_1009_3(self, arr: List[int]) -> bool:
		arr = sorted(arr)
		for i in range(len(arr) - 2):
			if arr[i + 2] - arr[i + 1] != arr[i + 1] - arr[i]:
				return False
		return True