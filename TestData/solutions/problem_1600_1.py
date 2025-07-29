class Solution:
   def solution_1600_1(self, nums: List[int]) -> int:
       return reduce(lambda x,y: x|y, nums)

class Solution:
   def solution_1600_1(self, nums: List[int]) -> int:
       return reduce(or_, nums)

class Solution:
   def solution_1600_1(self, nums: List[int]) -> int:
       
       ans = 0
       for n in nums:
           ans |= n      
       return ans