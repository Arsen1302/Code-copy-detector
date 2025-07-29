class Solution:
    def solution_389_5(self, nums: List[int]) -> bool:
    	j = 0
    	for i in range(len(nums)-1):
    		if nums[i]-nums[i+1] > 0:
    			D = i
    			j += 1
    			if j == 2:
    				return False
    	if j == 0 or D == 0 or D == len(nums)-2:
    		return True
    	if (nums[D-1] <= nums[D] <= nums[D+2]) or (nums[D-1] <= nums[D+1] <= nums[D+2]):
    		return True
    	else:
    		return False
			
	- Python 3
	- Junaid Mansuri