class Solution:
    def solution_372_1(self, nums: List[int], k: int) -> float:
    	M = d = 0
    	for i in range(len(nums)-k):
    		d += nums[i+k] - nums[i]
    		if d > M: M = d
    	return (sum(nums[:k])+M)/k
		
		
- Python 3
- Junaid Mansuri