class Solution:
    def solution_763_5(self, arr1: List[int], arr2: List[int]) -> int:
    	M = 0
    	for c in [[1,1],[1,-1],[-1,1],[-1,-1]]:
    		m = float('inf')
    		for i in [arr1[i]*c[0]+arr2[i]*c[1]+i for i in range(len(arr1))]:
    			if i < m: m = i
    			if i - m > M: M = i - m
    	return M
		
		
- Python 3
- Junaid Mansuri