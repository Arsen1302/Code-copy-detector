class Solution:
	def solution_456_4(self, left: int, right: int) -> int:
		from collections import Counter

		ans = 0
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53]

		for i in range(left, right + 1):
			tmp = bin(i)[2:]
			count = Counter(tmp)

			if count["1"] in primes:
				  ans += 1




		return ans