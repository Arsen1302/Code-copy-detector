class Solution:
    def solution_1263_2(self, nums: List[int]) -> int:
        mod=int(1e9+7)
        stack=[] # (index, prefix sum at index)
        rsum=0
        res=0
        
        nums.append(0)
        
        for i, v in enumerate(nums):
            while stack and nums[stack[-1][0]] >= v:
                index, _ = stack.pop()
				
				# if the stack is empty, the subarray sum is the current prefixsum
                arrSum=rsum
                
                if stack:
                    arrSum=rsum-stack[-1][1]
                
				# update res with subarray sum
                res=max(res, nums[index]*arrSum)
                
            rsum+=v
            stack.append((i, rsum))
        
        return res%mod