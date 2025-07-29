class Solution:

 def solution_1480_1(self, nums: List[int], original: int) -> int:

    while original in nums:
	
        original *= 2
		
    return original