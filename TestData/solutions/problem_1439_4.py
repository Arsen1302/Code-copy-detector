class Solution:
    def solution_1439_4(self, bombs: List[List[int]]) -> int:
        groups = []
        
        for i in range(len(bombs)):
          ix, iy, dis = bombs[i]
          target = []
          for j in range(len(bombs)):
            jx, jy, disj = bombs[j]
            if (ix - jx)**2 + (iy - jy)**2 <= dis**2:
              target.append(j)
          groups.append(target)
          
        res = 1
        
        for i in range(len(bombs)):
          visited = set()
          visited.add(i)
          start = [i]
          while start:
            new_start = []
            for element in start:
              for target in groups[element]:
                if target not in visited:
                  new_start.append(target)
                  visited.add(target)
            start = new_start
          res = max(res, len(visited))
        return res