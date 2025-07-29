class Solution:
    def solution_1710_4(self, nums: List[int]) -> List[int]:
        
        #apply the operations
        for idx, num in enumerate(nums[1:]):
            if nums[idx] == num:
                nums[idx] *= 2
                nums[idx+1] = 0
        
        # find the first zero
        for first_zero, num in enumerate(nums):
            if not num: break
        
        # check if there are any to shift
        if first_zero == len(nums) - 1: return nums

        # go through the array and shift numbers to the left
        for idx, num in enumerate(nums[first_zero+1:], first_zero+1):
            
            # we found a valid number after the zero so we need to switch it
            if num:
                nums[first_zero] = num
                nums[idx] = 0
            
            # go further with our first zero counter
            while first_zero < len(nums) and nums[first_zero]:
                first_zero += 1
            
            # check if we went out of bounds
            if first_zero > len(nums) - 1: break

        return nums