class Solution:
   def solution_1235_5(self, s: str, k: int) -> str:
       res = s.split()
       return ' '.join(res[:k])