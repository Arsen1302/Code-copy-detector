class Solution:
	def solution_91_3(self, n: int) -> bool:

		if n == 1:
			return True

		s = set()
		s.add(n)
		while True:
			count = 0
			for i in str(n):
				count += int(i) ** 2


			if count == 1:
				return True

			if count in s:
				break
			s.add(count)
			n = count

		return False