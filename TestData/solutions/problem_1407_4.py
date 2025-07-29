class Solution:
    def solution_1407_4(self, nums: List[int]) -> int:
        return min([k[0] for k in list(enumerate (nums)) if k[0]%10 == k[1]], default=-1)