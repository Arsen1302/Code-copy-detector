class Solution:
    def solution_371_5(self, E: str) -> str:
    	[a,b] = (lambda x: [x.real, x.imag])(eval(E.replace('x','j').replace('=','-(')+')', {'j': 1j}))
    	return 'x=' + str(int(-a//b)) if b else 'Infinite solutions' if not a else 'No solution'
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com