class Solution:
    def solution_447_2(self, nums: List[int]) -> int:
        largest = max(nums)
        for idx, val in enumerate(nums):
            if val==largest:
                new_idx = idx
                continue
            if val*2>largest: return -1
        return new_idx