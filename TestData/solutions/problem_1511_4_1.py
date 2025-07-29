class Solution:
    def solution_1511_4_1(self, nums: List[int], k: int) -> int:
        
        # define range sum
        def solution_1511_4_2(start, stop, step=1):
            number_of_terms = (stop - start) // step
            sum_of_extrema = start + (stop - step)
            return number_of_terms * sum_of_extrema // 2
        
        nums = list(set(nums)) # remove repeats
        nums.sort() # O(nlogn)
        
        # total sum
        sol = 0
        
        prev = 0
        ptr = 0
        
        while k > 0:
            if ptr < len(nums):
                # potential window to add nums
                gap = nums[ptr] - prev - 1
                
                sol += solution_1511_4_2(prev+1, min(nums[ptr], prev+k+1)) # add range sum O(1)
                
                k -= gap
                prev = nums[ptr]
                ptr += 1
            else: # draw numbers after all numbers in the list
                sol += solution_1511_4_2(prev+1, prev + remaining + 1)
                k = 0
        
        return sol