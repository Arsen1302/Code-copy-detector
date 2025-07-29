class Solution:
    def solution_1220_5(self, nums: List[int], k: int) -> int:
        nums = [0] + nums + [0]
        i = j = k+1
        res, n = 0, nums[i]

        while n:
            while n <= nums[i]: i -= 1
            while n <= nums[j]: j += 1
            res = max(res, n * (j-i-1))
            n = max(nums[i], nums[j])
        
        return res