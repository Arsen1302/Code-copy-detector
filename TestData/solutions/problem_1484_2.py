class Solution:
  def solution_1484_2(self, nums: List[int], pivot: int) -> List[int]:
    less = 0
    equal = 0
    
    for n in nums :
      if   n <  pivot : less  += 1
      elif n == pivot : equal += 1
    
    greater = less + equal
    equal   = less
    less    = 0
    
    ans = [0]*len(nums)
    
    for n in nums :
      if   n <  pivot :
        ans[less] = n
        less += 1
      elif n == pivot : 
        ans[equal] = n
        equal += 1
      else :
        ans[greater] = n
        greater += 1
        
    return ans