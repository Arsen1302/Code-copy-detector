class Solution:
    def solution_141_2(self, nums: List[int]) -> int:
    	t, h = nums[0], nums[nums[0]]
    	while t != h: t, h = nums[t], nums[nums[h]]
    	t = 0
    	while t != h: t, h = nums[t], nums[h]
    	return t
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com