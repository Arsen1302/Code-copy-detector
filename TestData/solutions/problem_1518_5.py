class Solution:
    def solution_1518_5(self, nums: List[int]) -> bool:
        for num in set(nums):
            if nums.count(num) % 2 != 0:
                return False
        return True