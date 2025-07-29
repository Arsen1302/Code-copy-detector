class Solution:
    def solution_431_4(self, nums: List[int]) -> int:
        
        # We'll assume the right sum as sum of all the elements in the list.
        right_sum = sum(nums)
        
        # We'll assume the left sum as 0.
        left_sum = 0
        
        # Now we'll iterate in the whole list
        for i in range(len(nums)):
            
            # We'll decrease the current value of the element from the right sum
            right_sum = right_sum-nums[i]
            
            # Now we'll check if left sum is equal to the right sum
            if(left_sum==right_sum):
                
                # If they both are equal then that means this is the pivot index and we've to return the value of i or the index value
                return i
            
            # If not then we'll add the current value of the element to the left sum and again go in the loop.
            left_sum = left_sum+nums[i]
        
        # If the loop is over and till now none of the condition is satisfied then we'll return -1.
        return -1