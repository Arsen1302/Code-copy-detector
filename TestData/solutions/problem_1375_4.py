class Solution:
	def solution_1375_4(self, nums: List[int]) -> int:
		n = len(nums)
		left = [-1 for i in range(n)]
		right = [-1 for i in range(n)]
		mx = -1
		for i in range(n):
			left[i] = mx
			mx = max(mx, nums[i])
		mx = 10**9
		for i in range(n-1,-1,-1):
			right[i] = mx
			mx = min(mx, nums[i])
		# print(left)
		# print(right)
		res = 0
		for i in range(1, n-1):
			if left[i] < nums[i] < right[i]:
				res += 2
			elif nums[i - 1] < nums[i] < nums[i + 1]:
				res += 1
		return res