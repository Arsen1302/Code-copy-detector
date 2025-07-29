class Solution:
    def solution_1634_4(self, nums: List[int]) -> int:
        ret = 0
        i = len(nums) - 1
        R = float('inf')
        while i >= 0:
            num_of_splits = (nums[i] - 1) // R
            ret += num_of_splits
            R = nums[i] // (num_of_splits + 1)
            i -= 1
        return int(ret)