class Solution:
    def solution_1375_5(self, nums: List[int]) -> int:
        n = len(nums)
        minFromRight = [0] * n
        curMin = nums[-1]
        for i in range(n-2, 0, -1):
            minFromRight[i] = curMin
            curMin = min(curMin, nums[i])
        
        res = 0
        curMax = nums[0]
        for i in range(1, n-1):
            if curMax < nums[i] < minFromRight[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            
            curMax = max(curMax, nums[i])
        
        return res