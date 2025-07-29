class Solution:
    def solution_1244_4(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [0] * len(nums)
        x = (2**maximumBit-1)
        for i, n in enumerate(nums):
            x = x ^ n
            ans[-1-i] = x
        return ans