class Solution:
    def solution_1524_5_1(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
      bobArrows = [x+1 for x in aliceArrows]
      
      def solution_1524_5_2(length):
        if length == 0: return ['']
        else:
          return ['1' + x for x in solution_1524_5_2(length-1)] + \
                 ['0' + x for x in solution_1524_5_2(length-1)]
        
      configs = solution_1524_5_2(11)
      
      score, res = -sys.maxsize, None
      for con in configs:
        arrow_needed = sum([bobArrows[x+1] for x in range(11) if con[x] == '1'])
        if arrow_needed <= numArrows:
          temp_score = sum([x+1 for x in range(11) if con[x] == '1'])
          if temp_score > score:
            score = temp_score
            res = [numArrows - arrow_needed] + [bobArrows[x+1] if con[x] == '1' else 0 for x in range(11)]
      return res
        
      
      #dp knapsack + backtrack
      #grid = [([[0, 0] for x in range(12)]) for _ in range(numArrows+1)]
      
      #aliceArrows = [x + 1 for x in aliceArrows]

      #for t in range(1, 12):
      #  target = aliceArrows[t]
      #  for k in range(numArrows+1):
      #    if k >= target:
      #      if grid[k-target][t-1][0] + t >= grid[k][t-1][0]:
      #        grid[k][t][0] = grid[k-target][t-1][0] + t
      #        grid[k][t][1] = target
      #      else:
      #        grid[k][t][0] = grid[k][t-1][0]
      #    else:
      #      grid[k][t][0] = grid[k][t-1][0]
          
      #res = []
       
      #for t in range(11, 0, -1):
      #  score, choice = grid[numArrows][t]
      #  res.append(choice)
      #  numArrows -= choice
      #res.append(numArrows)
      
      #return res[::-1]