class Solution:
    def solution_1637_4(self, nums: List[int]) -> bool:
      
      grid = [0] * (len(nums) + 1)
      grid[0] = 1
      
      if nums[0] == nums[1]:
        grid[2] = 1
        
      for t in range(3, len(nums)+1):
        if nums[t-1] == nums[t-2]:
          grid[t] = (grid[t-2] or grid[t])
        if nums[t-1] == nums[t-2] == nums[t-3] or \
           nums[t-1] == nums[t-2] + 1 == nums[t-3] + 2:
          grid[t] = (grid[t-3] or grid[t])
          
      return grid[-1]