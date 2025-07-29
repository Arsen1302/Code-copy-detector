class Solution:
    def solution_255_4(self, nums: List[int]) -> bool:
        mi = [nums[0]]
        
        n=len(nums)
        
        # making a min stack which store the minimum element till the current index from left
        for j in range(1,n):
            mi.append( min(mi[-1],nums[j]) )
            
            
        stack=[]
        
        
        for j in range(n-1,-1,-1):
            
            # makeing stack for the nums[k]
            
            while stack and stack[-1]<=mi[j]:
                stack.pop()
            if len(stack)>0:
                if mi[j]<stack[-1]<nums[j]:
                    return True
            stack.append(nums[j])
        
        return False