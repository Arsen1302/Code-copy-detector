class Solution:
    def solution_769_1_1(self, nums: List[int]) -> int:
        def solution_769_1_2(nums, small_first=True):
            if n <= 1: return 0
            ans = 0
            for i in range(n-1):
                if small_first and nums[i] >= nums[i+1]:
                    ans += nums[i] - (nums[i+1]-1)
                    nums[i] = nums[i+1] - 1
                elif not small_first and nums[i] <= nums[i+1]:
                    ans += nums[i+1] - (nums[i]-1)
                    nums[i+1] = nums[i] - 1
                small_first = not small_first
            return ans    
        n = len(nums)
        return min(solution_769_1_2(nums[:], True), solution_769_1_2(nums[:], False))