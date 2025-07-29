class Solution:
    def solution_1007_5(self, nums: List[int], target: int) -> int:
        
        # sort 
        nums.sort()
        
        # easy corner case
        if nums[0] > target:
            return 0
       
        # preprocess the nums to remove useless numbers that are already greater than target
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        nums = nums[:left]
        
        # regular two-pointer move
        right = left-1
        left = 0
        result = 0
        mod = (10**9 + 7)
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow(2, right - left, mod)
                left += 1
            else:
                right -= 1
    
        return result % mod