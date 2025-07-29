class Solution:
    def solution_769_3(self, nums: List[int]) -> int:
        moves_even, moves_odd = 0, 0
        ldec_even, ldec_odd = 0, 0
        
        if len(nums) > 1:
            moves_even += max(0, nums[1] - nums[0] + 1)
            ldec_even = moves_even
            
        for i, num in enumerate(nums[1:], 1):
            if i % 2 == 0:
                # even
                moves_even += max(0, nums[i-1] - num - ldec_even + 1)
                if i+1 < len(nums):
                    ldec_even = max(0, nums[i+1] - num + 1) 
                    moves_even += ldec_even
            else:
                # odd
                moves_odd += max(0, nums[i-1] - num - ldec_odd + 1)
                if i+1 < len(nums):
                    ldec_odd = max(0, nums[i+1] - num + 1) 
                    moves_odd += ldec_odd
        
        return min(moves_even, moves_odd)