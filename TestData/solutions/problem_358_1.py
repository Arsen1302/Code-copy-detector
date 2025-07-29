class Solution:
    def solution_358_1(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)): 
            lo, hi = 0, i-1
            while lo < hi: 
                if nums[lo] + nums[hi] > nums[i]:
                    ans += hi - lo 
                    hi -= 1
                else: lo += 1
        return ans