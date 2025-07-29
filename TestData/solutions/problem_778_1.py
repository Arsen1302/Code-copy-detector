class Solution:
    def solution_778_1(self, s: str) -> str:
    	S, L, a = [ord(i) for i in s] + [0], len(s), 1
    	M = max(S)
    	I = [i for i in range(L) if S[i] == M]
    	if len(I) == L: return s
    	while len(I) != 1:
    		b = [S[i + a] for i in I]
    		M, a = max(b), a + 1
    		I = [I[i] for i, j in enumerate(b) if j == M]
    	return s[I[0]:]
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com