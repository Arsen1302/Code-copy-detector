class Solution:
  def solution_904_2_1(self, digits: List[int]) -> str:

    digits.sort()
    rem = [d % 3 for d in digits]
    s = sum(rem) % 3

    def solution_904_2_2(x): 
      idx = rem.index(x)
      del digits[idx]
      del rem[idx]

    if s != 0:
      try:
        solution_904_2_2(s)
      except ValueError:
        solution_904_2_2(3-s)
        solution_904_2_2(3-s)

    if len(digits) == 0: return "" 
    if digits[-1] == 0: return "0"
    return ("".join(str(d) for d in reversed(digits)))