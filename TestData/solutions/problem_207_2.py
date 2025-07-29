class Solution:
    def solution_207_2(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        rotate_sum = 0
        
        for i in range(n):
            rotate_sum += nums[i] * i       # ex. [0, 1, 2, 3]  --> 0*0 + 1*1 + 2*2 + 3*3
            
        res = rotate_sum
        
        for i in range(n-1, 0 , -1):
            rotate_sum += s - n * nums[i]   # 0*0 + 1*1 + 2*2 + 3*3 --> 0*1 + 1*2 + 2*3 + 3*4 --> 0*1 + 1*2 + 2*3 + 3*0
            res = max(res, rotate_sum)      # update res
            
        return res