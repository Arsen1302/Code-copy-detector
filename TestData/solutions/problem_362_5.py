class Solution:
    def solution_362_5(self, n: List[int]) -> int:
    	n.sort()
    	return max(n[-1]*n[0]*n[1], n[-1]*n[-2]*n[-3])