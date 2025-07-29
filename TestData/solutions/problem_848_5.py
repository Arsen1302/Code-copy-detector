class Solution:
    def solution_848_5(self, N: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in N)
		
		
- Junaid Mansuri
- Chicago, IL