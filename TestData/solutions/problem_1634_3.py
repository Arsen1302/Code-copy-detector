class Solution:
    def solution_1634_3(self, nums: List[int]) -> int:
        res = 0
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
                continue
            q, r = divmod(nums[i], prev)
            ops = q if r else q - 1
            res += ops
            prev = nums[i] // (ops + 1)
            
        return res