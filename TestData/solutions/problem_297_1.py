class Solution:
    def solution_297_1(self, N: int) -> int:
    	a, b = 0, 1
    	for i in range(N): a, b = b, a + b
    	return a
		
		
- Python 3
- Junaid Mansuri