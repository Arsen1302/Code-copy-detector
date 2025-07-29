class Solution:
    def solution_406_5(self, nums: List[int], k: int) -> List[int]:
        ans = 0
        n = len(nums)

        #stores the sum of maximum sum subarray of lenght k for starting 
        dp1 = [0]*len(nums)
        
        #stores the sum of maximum sum subarray of lenght k for ending
        dp2 = [0]*len(nums)
        
        sum2 = 0
        for i in range(len(nums)):
            if i < k:
                sum2 += nums[i] 
                dp1[i] = sum2
            else:
                sum2 += nums[i] - nums[i-k]
                dp1[i] = max(dp1[i-1],sum2) 
        sum1 = 0
        for j in range(n-1,-1,-1):
            if j+k >= n:
                sum1 += nums[j]
                dp2[j] = sum1
            else:
                sum1 += nums[j] - nums[j+k]
                dp2[j] = max(dp2[j+1],sum1)
        left = -1
        middle = -1
        right = -1
        for i in range(k,n-2*k+1):
            if dp1[i-1] + sum(nums[i:i+k]) + dp2[i+k] > ans:
                ans = dp1[i-1] + sum(nums[i:i+k]) + dp2[i+k]
                leftsum = dp1[i-1]
                rightsum = dp2[i+k]
                middle = i
        
        for i in range(n):
            if sum(nums[i:i+k])== leftsum:
                left = i
                break

        for j in range(middle+k,n):
            if sum(nums[j:j+k]) == rightsum:
                right = j
                break
        return [left,middle,right]