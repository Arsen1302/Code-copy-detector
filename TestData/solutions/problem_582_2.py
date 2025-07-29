class Solution:
    def solution_582_2(self, nums: List[int]) -> bool:
        a = sorted(nums)
        b = sorted(nums,reverse=True)
        if nums == a or nums == b:
            return True
        return False