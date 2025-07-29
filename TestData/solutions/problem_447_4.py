class Solution:
    def solution_447_4(self, nums):
        if len(nums) == 1: return 0
        s = sorted(nums, reverse=True)
        largest, secondLargest = s[0], s[1]
        return nums.index(largest) if largest >= 2*secondLargest else -1