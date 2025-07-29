class Solution:
    def solution_944_3(self, nums: List[int]) -> int:
        prefix_sum = 0 # taking this variable to store prefix sum
        min_start_value = 1 # as stated in the question min startValue shouldn`t be less then 1.
        
        for num in nums: # traversing through the provided list
            prefix_sum += num # calculating prefix sum
            min_start_value = max(min_start_value, 1-prefix_sum) # Taking max as value shouldnt be less them 1. Subtracting 1 to convert the negetives to positives.
        return min_start_value