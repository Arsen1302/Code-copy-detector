class Solution:
    def solution_372_4(self, nums: List[int], k: int) -> float:
        

        window_sum=0
        for i in range(0,k):
            window_sum=window_sum+nums[i]
        max_sum=window_sum
        start=0
        for j in range(k,len(nums)):
            window_sum=window_sum-nums[start]+nums[j]
            # if window_sum<0:
            #     window_sum=0
            max_sum=max(max_sum,window_sum)
            start=start+1
        return max_sum/k