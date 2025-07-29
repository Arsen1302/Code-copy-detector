class Solution:
  def solution_1025_1(self, low: int, high: int) -> int:
    if low % 2 == 0:
      return (high-low+1)//2
    return (high-low)//2 + 1