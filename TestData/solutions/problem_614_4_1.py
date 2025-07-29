class Solution:
    def solution_614_4_1(self, N: int) -> List[int]:
        
        def solution_614_4_2(nums): 
            """Return beautiful array by rearraning elements in nums."""
            if len(nums) <= 1: return nums
            return solution_614_4_2(nums[::2]) + solution_614_4_2(nums[1::2])
        
        return solution_614_4_2(list(range(1, N+1)))