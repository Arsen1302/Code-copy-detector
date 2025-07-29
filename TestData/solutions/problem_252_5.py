class Solution:
	def solution_252_5(self, nums: List[int]) -> int:
		_sum, _min = 0, float('inf')
		for num in nums:
			_sum += num
			_min = _min if _min < num else num
		return _sum-_min*len(nums)