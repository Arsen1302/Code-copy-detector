class Solution:
    def solution_1677_2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        non_inc_prefix = [1] * n
        for i in range(1, n-1):
            if nums[i-1] >= nums[i]:
                non_inc_prefix[i] += non_inc_prefix[i-1]
                
        non_dec_suffix = [1] * n
        for i in range(n-2, 0, -1):
            if nums[i] <= nums[i+1]:
                non_dec_suffix[i] += non_dec_suffix[i+1]

        good = []
        for i in range(k, n - k):
            if non_inc_prefix[i-1] >= k <= non_dec_suffix[i+1]:
                good.append(i)
        
        return good