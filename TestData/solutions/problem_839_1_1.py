class Solution:
    def solution_839_1_1(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            div_sum =  self.solution_839_1_2(mid, nums)
            if div_sum > threshold:
                left = mid
            else:
                right = mid
        
        div_sum = self.solution_839_1_2(left, nums)
        if div_sum <= threshold:
            return left
        return right
        
    
    def solution_839_1_2(self, divisor, nums):
        res = 0
        for n in nums:
            tmp = n // divisor
            if tmp * divisor < n:
                tmp += 1
            
            res += tmp
        
        return res