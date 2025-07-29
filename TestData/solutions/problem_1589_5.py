class Solution:
    def solution_1589_5(self, nums: List[int], k: int) -> int:
        start = 0 
        end = 0
        N = len(nums)
        rolling_sum = 0 
        ans = 0
        
        for idx, value in enumerate(nums):
            rolling_sum += value
            window_size = end-start
            
            while start < end and rolling_sum * (end-start+1) >= k:
                rolling_sum -= nums[start]
                start += 1
                window_size -= 1
            
            window_size = end-start

            if rolling_sum * (window_size+1) < k:
                ans += window_size if window_size >= 0 else 0
            
            # add single self array
            if value < k:
                ans += 1
                
            end += 1
        
        return ans