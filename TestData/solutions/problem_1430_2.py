class Solution:
    def solution_1430_2(self, nums: List[int], k: int) -> List[int]:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = [-1]*len(nums)
        for i, x in enumerate(nums): 
            if k <= i < len(nums)-k: ans[i] = (prefix[i+k+1] - prefix[i-k])//(2*k+1)
        return ans