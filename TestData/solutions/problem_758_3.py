class Solution:
    def solution_758_3(self, h: List[int]) -> int:
        h, M, D = list(itertools.accumulate([2*(i > 8)-1 for i in h])), 0, {}
        for i, s in enumerate(h):
        	if s > 0: M = i + 1
        	elif s - 1 in D: M = max(M, i - D[s-1])
        	elif s not in D: D[s] = i
        return M
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com