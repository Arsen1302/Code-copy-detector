class Solution:
    def solution_684_4(self, nums: List[int], k: int) -> int:
        firstStart, secondStart = 0, 0
        
        maxWindow = float('-inf')
        
        while firstStart < len(nums):
            if nums[firstStart] == 0:
                k -= 1
                
            if k < 0:
                if nums[secondStart] == 0:
                    k += 1
                secondStart += 1
            
            firstStart += 1
            
            maxWindow = max(maxWindow, (firstStart - secondStart))
            
        return maxWindow