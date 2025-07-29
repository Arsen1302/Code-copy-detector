class Solution:
    def solution_319_2(self, nums: List[int]) -> int:
        val, seen = -1, True
        for num in nums:
            if val == num:
                seen = True
            elif seen:
                val = num
                seen = False
            else:
                return val
        return -1  # this will never be reached