class Solution:
	def solution_5_3_1(self, s: str) -> str:
		res = ""
		length = len(s)
		def solution_5_3_2(left: int, right: int):
			while left >= 0 and right < length and s[left] == s[right]:
				left -= 1
				right += 1
				
			return s[left + 1 : right]
		
		
		for index in range(len(s)):
			res = max(solution_5_3_2(index, index), solution_5_3_2(index, index + 1), res, key = len)
			
		return res