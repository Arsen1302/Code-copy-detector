class Solution:
    def solution_686_3(self, N: int) -> int:
    	a, n, b = 0, N, N >= 4
    	if b: a, n = n*(n-1)//(n-2)+(n-3), n - 4
    	while n >= 4: a, n = a - n*(n-1)//(n-2)+(n-3), n - 4
    	return a + [0,-1,-2,-6][n]*(2*b-1)
		


- Junaid Mansuri
(LeetCode ID)@hotmail.com