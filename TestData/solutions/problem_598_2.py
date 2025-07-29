class Solution:
	def solution_598_2(self, nums: List[int]) -> int:
		lng = len(nums)
		maxx, minn = nums[0], min(nums[1:])
    
		for i in range(lng):
			maxx = max(maxx, nums[i])
			if minn == nums[i]: minn = min(nums[i + 1:])
			if maxx <= minn: return i + 1