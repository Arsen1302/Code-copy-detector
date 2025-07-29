class Solution:
    def solution_375_3_1(self, s: str) -> int:
		def solution_375_3_2(left: int, right: int) -> int:
		    count = 0
			while left >= 0 and right < len(s) and s[left] == s[right]:
			    # count the palindrome and solution_375_3_2 outward
			    count += 1
				left -= 1
				right += 1
			return count
		
		palindromes = 0
		for i in range(len(s)):
		    # the idea is to solution_375_3_2 around the 'center' of the string, but the center could be 1 or 2 letters
			# e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
		    palindromes += solution_375_3_2(i, i)
			palindromes += solution_375_3_2(i, i+ 1)
		return palindromes