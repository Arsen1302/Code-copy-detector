class Solution:
    def solution_1554_2(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        left, right = 0, len(nums)
        min_value, return_idx= abs(right_sum//right), len(nums)-1
        
        for i in range(0,len(nums) - 1):
            left_sum += nums[i]
            left+=1
            right_sum -= nums[i]
            right -=1
            curr = abs(left_sum//left - right_sum//right)
            if min_value > curr or (min_value == curr and i < return_idx):
                min_value = curr
                return_idx = i
        
        return return_idx