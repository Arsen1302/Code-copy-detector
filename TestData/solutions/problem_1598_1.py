class Solution:
	"""
	Time:   O(n)
	Memory: O(1)
	"""

	def solution_1598_1(self, s: str) -> int:
		is_closed = True
		count = 0

		for c in s:
			count += is_closed * c == '*'
			is_closed ^= c == '|'

		return count


class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def solution_1598_1(self, s: str) -> int:
		return sum(chunk.count('*') for chunk in s.split('|')[0::2])