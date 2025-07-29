class Solution:
    def solution_1244_1(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        for i in range(1,len(nums)):
            res.append(2**maximumBit - 1 - nums[i-1])
            nums[i] = nums[i-1]^nums[i]
        res.append(2**maximumBit - 1 - nums[-1])
        return res[::-1]