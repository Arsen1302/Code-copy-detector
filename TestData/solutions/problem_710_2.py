class Solution:
    def solution_710_2(self, R: int, C: int, r: int, c: int) -> List[List[int]]:
    	return sorted([[i,j] for i in range(R) for j in range(C)], key = lambda y: abs(y[0]-r)+abs(y[1]-c))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com