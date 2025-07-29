class Solution:
    def solution_1263_3(self, nums: List[int]) -> int:
        n,ans=len(nums),-float('inf')
        mod=10**9+7
        left=[0 for i in range(n)]
        right=[0 for i in range(n)]
        prefixSum=[0 for i in range(n)]
        prefixSum[0]=nums[0]
        for i in range(1,n):
            prefixSum[i]+=prefixSum[i-1]+nums[i]
        stack=[]
        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            left[i]=stack[-1] if len(stack) else -1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            right[i]=stack[-1]-1 if len(stack) else n-1
            stack.append(i)
        for i in range(n):
            currMax=prefixSum[right[i]]-(prefixSum[left[i]] if left[i]!=-1 else 0)
            ans=max(ans,currMax*nums[i])
        return ans%mod