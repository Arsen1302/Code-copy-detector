class Solution:
    def solution_1710_5(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                i += 1
            else:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
        return [x for x in nums if x] + [0]*nums.count(0)