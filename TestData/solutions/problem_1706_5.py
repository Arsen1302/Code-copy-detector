class Solution:
    def solution_1706_5(self, nums: List[int]) -> int:
        valid_nums = [num for num in nums if num % 3 == 0 and num % 2 == 0]
        if len(valid_nums) == 0:
            return 0
        return int(sum(valid_nums)/len(valid_nums))