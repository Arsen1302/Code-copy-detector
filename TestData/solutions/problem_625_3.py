class Solution:
    def solution_625_3(self, A: List[str]) -> int:
    	return sum(list(i) != sorted(i) for i in zip(*A))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com