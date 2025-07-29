class Solution:
	def solution_252_3(self, nums: List[int]) -> int:
		_min, _sum = min(nums), 0
		for num in nums:
			_sum += num-_min  # for num->_min, -1 per move takes (num-_min) moves
		return _sum