class Solution:
    def solution_328_3(self, W: List[List[int]]) -> int:
    	L, C = len(W), collections.defaultdict(int)
    	for w in W:
    		s = 0
    		for b in w: s += b; C[s] += 1
    	C[s] = 0
    	return L - max(C.values())