class Solution:
    def solution_1124_2(self, nums: List[int]) -> int:
        odd, even = 0, 0
        for i in range(len(nums)):
            if i % 2:
                odd += nums[i]
            else:
                even += nums[i]
        
        ret = 0

        left_even = left_odd = 0
        for i in range(len(nums)):
            if not i % 2:
                even -= nums[i]
                if left_even + odd == left_odd + even:
                    ret += 1
                left_even += nums[i]
            else:
                odd -= nums[i]
                if left_odd + even == left_even + odd:
                    ret += 1
                left_odd += nums[i]
            
        return ret