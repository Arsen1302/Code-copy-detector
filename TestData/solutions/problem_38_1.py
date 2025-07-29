class Solution:
    def solution_38_1(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]