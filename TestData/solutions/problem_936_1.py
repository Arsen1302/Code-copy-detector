class Solution:
    def solution_936_1(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = []
        while sum(l) <= sum(nums):
            l.append(nums.pop())
        return l