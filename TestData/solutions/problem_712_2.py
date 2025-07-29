class Solution:
    def solution_712_2(self, a: int, b: int, c: int) -> List[int]:
    	[a,b,c] = sorted([a,b,c])
    	return [1 if 2 in [b-a,c-b] else (0 + (b-a != 1) + (c-b != 1)), c-a-2]
		
		
- Junaid Mansuri
(LeeCode ID)@hotmail.com