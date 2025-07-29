class Solution:
    def solution_1585_2(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {} 
        for i,num in enumerate(nums):
            d[num] = i #Save index of all elements in dictionary for O(1) lookup
        
        for x,r in operations:
            where = d[x] # Find location of operation from dictionary
            nums[where] = r # Complete the operation (Change number)
            del d[x]   # Update dictionary
            d[r] = where # Update dictionary
            
        return nums