class Solution:
	"""
	Time:   O(2^n)
	Memory: O(2^n)
	"""

	def solution_648_4(self, n: int, k: int) -> List[int]:
		nums = list(range(1, 10))

		for i in range(1, n):
			nums = [num * 10 + d for num in nums for d in {num % 10 + k, num % 10 - k} if 0 <= d <= 9]

		return nums