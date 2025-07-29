class Solution:
    def solution_1484_4(self, nums: List[int], pivot: int) -> List[int]:

        #left side:
        i = 0
        left = []
        while i < len(nums):
            if nums[i] < pivot:
                left.append(nums[i])
            i += 1
        
        #right side:
        i = 0
        right = []
        while i < len(nums):
            if nums[i] > pivot:
                right.append(nums[i])
            i += 1
        
        #pivot and equals to it
        i = 0
        pivot_equals = []
        while i < len(nums):
            if nums[i] == pivot:
                pivot_equals.append(nums[i])
            i += 1
        
        nums = left + pivot_equals + right
        return nums