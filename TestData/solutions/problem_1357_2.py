class Solution:
    def solution_1357_2(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=int)[-k]