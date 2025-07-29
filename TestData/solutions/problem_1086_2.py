class Solution:
    def solution_1086_2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n<=nums[0]:
            return n
        
        #binary search
        start,end = 0,n
                
        while(start<=end):
            mid = (start+end)//2
            #index of middle element
            count = 0
            for i in range(0,n):
                if nums[i]>=mid:
                    count = n-i
                    #count+=1 could use this but will take more iterations then.
                    break
        
            if count==mid:
                return count
            elif count<mid:
                end = mid-1
            else:
                start=mid+1            
        
        return -1