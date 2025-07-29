class Solution:
    def solution_698_1(self, A: List[int]) -> List[bool]:
    	n = 0
    	for i in range(len(A)): A[i], n = (2*n + A[i]) % 5 == 0, (2*n + A[i]) % 5
    	return A
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com