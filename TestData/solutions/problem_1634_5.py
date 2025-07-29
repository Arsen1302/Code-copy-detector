class Solution:
    def solution_1634_5(self, nums: List[int]) -> int:
        
        ref = nums[-1]
        n = len(nums)
        res = 0
        for i in range(n-2, -1, -1):
            if nums[i] <= ref:
                ref = nums[i]
                continue
            q, r = divmod(nums[i], ref)
            
            # 1-item in strategy
            if r == 0:
                res += q - 1
            # 2-item in strategy
            else:
                res += q
                ref = nums[i] // (q + 1)
                
        return res