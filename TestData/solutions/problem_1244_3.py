class Solution:
    def solution_1244_3(self, nums: List[int], maximumBit: int) -> List[int]:        
        return list(accumulate([nums[0] ^ (1 << maximumBit) - 1] + nums[1:], ixor))[::-1]