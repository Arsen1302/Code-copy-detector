class Solution:
    def solution_1695_5(self, nums: List[int]) -> int:
        return len(set(nums+[int(str(n)[::-1]) for n in nums]))