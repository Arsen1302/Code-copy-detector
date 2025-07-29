class Solution:
    def solution_355_1(self, f: List[int], n: int) -> bool:
        L, i, c, f = len(f)-2, -2, 0, f + [0]
        while i < L:
        	i += 2
        	if f[i] == 1: continue
        	if f[i+1] == 0: c += 1
        	else: i += 1
        return n <= c
		
		
		
		
class Solution:
    def solution_355_1(self, f: List[int], n: int) -> bool:
    	L, f, i, c = len(f), [0] + f + [0], 1, 0
    	while i <= L:
    		if f[i-1:i+2] == [0,0,0]: c, i = c + 1, i + 1
    		i += 1
    	return n <= c
		
		
		
		
class Solution:
    def solution_355_1(self, f: List[int], n: int) -> bool:
    	L, f, s, c = len(f), f + [0,1], 0, 1
    	for i in range(L+2):
    		if f[i] == 1: s, c = s + max(0,c-1)//2, 0
    		else: c += 1
    	return n <= s
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com