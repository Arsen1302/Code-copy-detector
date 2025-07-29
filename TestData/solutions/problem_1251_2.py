class Solution:
    def solution_1251_2(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = 0 
        for i in reversed(range(len(nums))): 
            lo, hi = 0, i
            while lo < hi: 
                mid = lo + hi >> 1
                if nums[i] * (i - mid) + prefix[mid] - prefix[i] <= k: hi = mid
                else: lo = mid + 1
            ans = max(ans, i - lo + 1)
        return ans