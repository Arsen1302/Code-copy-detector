class Solution:
    def solution_352_2(self, m: int, n: int, p: List[List[int]]) -> int:
    	return min([i[0] for i in p])*min(i[1] for i in p) if p else m*n
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com