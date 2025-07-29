class Solution:
    def solution_66_1(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        if(nums[start] <= nums[end]):
            return nums[0]
        
        while start <= end:
            mid = (start + end) // 2
            
            if(nums[mid] > nums[mid+1]):
                return nums[mid+1]
            
            if(nums[mid-1] > nums[mid]):
                return nums[mid]
            
            if(nums[mid] > nums[0]):
                start = mid + 1
            else:
                end = mid - 1
                
        return nums[start]