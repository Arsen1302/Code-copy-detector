class Solution:
    def solution_1695_1(self, nums: List[int]) -> int:
        return len(set([int(str(i)[::-1]) for i in nums] + nums))