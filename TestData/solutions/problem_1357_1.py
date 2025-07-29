class Solution:
    def solution_1357_1(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums), reverse=True)
        return str(nums[k-1])