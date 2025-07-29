class Solution:
    def solution_839_5_1(self, nums: List[int], threshold: int) -> int:
        high = max(nums)
        low = 1
        while (low < high):
            
            mid = (low + high)//2
            
            if self.solution_839_5_2(nums, mid, threshold):
                high = mid
                
            else:
                low = mid + 1
                
                
        return low
        
        
    def solution_839_5_2(self, nums, thres, threshold):
        divSum = 0
        for i in range(len(nums)):
            divSum += math.ceil(nums[i]/thres)
            
        return (divSum <= threshold)