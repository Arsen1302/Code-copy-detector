class Solution:
    def solution_337_3(self, n: List[int]) -> int:
    	S = {}
    	for i in range(len(n)):
    		if n[i] == -1: continue
    		m, a = 0, i
    		while n[a] != -1: n[a], a, b, m = -1, n[a], a, m + 1
    		S[i] = m + S.pop(b, 0)
    	return max(S.values())


- Python 3
(LeetCode ID)@hotmail.com