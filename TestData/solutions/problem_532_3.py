class Solution:
    def solution_532_3(self, S: str, T: str) -> bool:
    	a, A = [[],[],0,0], [S,T]
    	for i in range(2):
    		for j in A[i][::-1]:
    			if j != '#':
    				if a[i+2] == 0: a[i].append(j)
    				else: a[i+2] -= 1
    			else: a[i+2] += 1
    	return a[0] == a[1]
		
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com