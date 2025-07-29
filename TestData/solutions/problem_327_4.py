class Solution:
    def solution_327_4(self, n: List[int]) -> str:
    	return f'{n[0]}/({"/".join(map(str,n[1:]))})' if len(n)>2 else "/".join(map(str,n))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com