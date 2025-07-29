class Solution:
    def solution_200_2(self, s: str, t: str) -> str:
    	for i in set(t):
    		if s.count(i) != t.count(i): return i