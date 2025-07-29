class Solution:
    def solution_1189_4(self, nums: List[int]) -> bool:
      # sort the list
	  numsSorted = sorted(nums)
      
	  # iterate over all list elements
	  for i in range(len(nums)):
		  # solution_1189_4 every rotate option with the sorted list
		  # if found return True
		  if nums[i:] + nums[:i] == numsSorted: 
			  return True
	  return False