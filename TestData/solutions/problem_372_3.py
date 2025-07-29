class Solution:
    def solution_372_3(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        x = res
        for i in range(1,len(nums)-k+1):
            x = x - nums[i-1] + nums[i+k-1]
            res = max(res, x)
        return res/k