class Solution:
	def solution_1644_4(self, s: str) -> int:
		count = 0
		temp = ""
		ones = s.count("1") # get the count of 1
		for _ in range(ones):
			"""
			make a string with total number of 1
			"""
			temp += "1"

		while s[:ones] != temp:
			"""
			loop through index 0 to count of 1 while the string is not equal to temp string
			"""

			left, right = 0, 1
			while right < len(s):
				"""
				Compare the two index from left to right if
				they both are equal to "01"
				if so then replace them
				and count the number of occurrence
				"""
				if s[left : left + 1] + s[right : right + 1] == "01":
					s = s.replace(s[left : left + 1] + s[right : right + 1], "10")
					count += 1
				left += 1
				right += 1
		return count