class Solution:
  def solution_1550_3(self, circles: List[List[int]]) -> int:
    table = set()
    
    for c in circles :
      xl = c[0] - c[2]
      xr = c[0] + c[2]
      yu = c[1]
      yd = c[1]
      step = 1
      r2 = c[2]*c[2]
      
      for x in range (xl, xr +1) : table.add((x<<8) + yu)
      while step <= c[2] :
        yu += 1
        yd -= 1
        x = int(math.sqrt(r2 - step*step))
        for X in range(c[0] - x, c[0] + x + 1) :
          table.add((X<<8) + yu)
          table.add((X<<8) + yd)
        step += 1
    
    return len(table)