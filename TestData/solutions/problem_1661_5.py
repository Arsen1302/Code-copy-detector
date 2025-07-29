class Solution:
    def solution_1661_5(self, nums: List[int]) -> int:
        left = res = mask = 0
        
        for right, num in enumerate(nums):
            while (mask &amp; num):  #while mask has set bits in same position as in num (stop once mask &amp; num == 0, so we can add num)
                mask ^= nums[left]  #using xor to remove the bits set by nums[left] (1 ^ 1 = 0)
                left += 1
            
            mask |= num  #setting the bits in mask that are set in nums
            res = max(res, right - left + 1)
            
        return res