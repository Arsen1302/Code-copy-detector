class Solution:
    def solution_798_2(self, s: str, t: str, M: int) -> int:
    	L, D, m, i, j = len(s)+1, [abs(ord(s[i])-ord(t[i])) for i in range(len(s))], 0, 0, 0
    	C = [0]+list(itertools.accumulate(D))
    	while i < L - m:
    		while j < L and C[j]-C[i] <= M: m, j = max(m, j - i), j + 1
    		i += 1
    	return m
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com