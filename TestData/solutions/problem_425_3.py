class Solution:
    def solution_425_3(self, b: List[int]) -> bool:
    	L, i = len(b)-1, 0
    	while i < L: i += 1 + b[i]
    	return True if i == L else False
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com