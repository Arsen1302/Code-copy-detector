class Solution:
    def solution_315_3_1(self, nums: List[int], k: int) -> int:
        def solution_315_3_2(l,h,k):
		
            while l <= h:
                
                mid = l+(h-l)//2

                if nums[mid] == k:            
                    return True

                if nums[mid] > k:
                    h = mid -1
                else:
                    l = mid + 1
            
            
        num_set,ans = set(nums),set()        
        nums.sort()
        N = len(nums)
        
        for pos,val in enumerate(nums):
            
            if val+k in num_set and solution_315_3_2(pos+1,N-1,val+k):
                
				ans.add((val, val+k))
				
        return len(ans)