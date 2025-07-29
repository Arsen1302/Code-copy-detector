class Solution:
    def solution_1589_4(self, nums: List[int], k: int) -> int:
        i, start = 0, 0
        n = len(nums)
        val, ans, sums = 1, 0, 0
        
        while i < n:
            sums += nums[i]
            val = sums * (i-start+1)
            while start <= i and val >= k:
                sums -= nums[start]
                start += 1
                val = sums * (i-start+1)
            ans += (i-start+1)
            i += 1
        
        return ans