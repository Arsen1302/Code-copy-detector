class Solution:
	def solution_555_4(self, n: int) -> int:
		max_ = 0

		num = str(bin(n)[2:])


		for i in range(len(num)):
			for j in range(i + 1, len(num)):
				if num[i] == "1" and num[j] == "1":
					max_ = max(max_, j - i)
					break


		return max_