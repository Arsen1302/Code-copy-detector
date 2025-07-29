class Solution:
    def solution_258_2(self, s: str) -> bool:
	# Here we checking that s is present in a new string double of s which after remvoing fast and last element
        return s in s[1:] + s[:-1]