class Solution:
    def solution_1465_3(self, nums: List[int]) -> int:
        l = r = 0
        zero = 0
        k = nums.count(1) + 1     #our window size #O(n)
        nums+=nums #double the array
        
        mi = len(nums)*3 #just random higher number
        
        while r < len(nums):
            if (r - l + 1) == k: #if our window size is k increment left and add the minimum size
                mi = min(mi, zero)
                if nums[l] == 0:
                    zero-=1
                l+=1
                
            if nums[r] == 0:
                zero+=1
            r+=1
        print(mi)
        
        return mi