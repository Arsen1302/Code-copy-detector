class Solution:
    def solution_955_5(self, nums: List[int], k: int) -> int:
        sw=deque()
        n=len(nums)
        currSum=0
        ans=-float('inf')
        for i in range(n):
            if sw and i-k>sw[0][0]:
                sw.popleft()
            if len(sw):
                currSum=max(nums[i],nums[i]+sw[0][1])
            else:
                currSum=nums[i]
            #print(currSum,sw)
            while sw and sw[-1][1]<=currSum:
                sw.pop()
            sw.append([i,currSum])
            ans=max(ans,currSum)
        return ans