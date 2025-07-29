class Solution:
    def solution_372_5(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0
        max_sum = 0
        if n == 1:
            return nums[0]/k
        if n == k:
            for i in range(0,n):
                curr_sum += nums[i]
            return curr_sum/k
            
        for i in range(0,k):
            curr_sum += nums[i]
        max_sum = curr_sum
        
        for i in range(k,n):
            curr_sum -= nums[i - k]
            curr_sum += nums[i]
            
            if max_sum < curr_sum:
                max_sum = curr_sum
            
            average = max_sum/k
            #avg = "{:.5f}".format(average)
        return average