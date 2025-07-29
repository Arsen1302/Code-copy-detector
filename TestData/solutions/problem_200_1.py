class Solution:
    def solution_200_1(self, s: str, t: str) -> str:
    	s, t = sorted(s), sorted(t)
    	for i,j in enumerate(s):
    		if j != t[i]: return t[i]
    	return t[-1]