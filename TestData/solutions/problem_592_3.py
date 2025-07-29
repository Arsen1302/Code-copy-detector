class Solution:
    def solution_592_3(self, A: List[int], K: int) -> int:
    	return max(0, max(A) - min(A) - 2*K)
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com