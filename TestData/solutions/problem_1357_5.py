class Solution:
    def solution_1357_5(self, nums: List[str], k: int) -> str:
        return sorted(nums, key = int, reverse = True)[k-1]