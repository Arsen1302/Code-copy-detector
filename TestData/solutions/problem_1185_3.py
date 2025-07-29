class Solution:
    def solution_1185_3(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            if nums.count(i) > 1 and i in s:
                s.remove(i)
        return sum(s)