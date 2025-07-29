class Solution:
    def solution_848_1(self, nums: List[int]) -> int:
        return len([x for x in nums if len(str(x)) % 2 == 0])