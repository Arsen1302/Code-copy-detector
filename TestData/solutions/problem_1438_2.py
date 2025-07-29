class Solution:
    def solution_1438_2(self, security: List[int], time: int) -> List[int]:

      grid1 = [0, 1]
      grid2 = [0, 1]

      for i in range(len(security)-1):
        if security[i] >= security[i+1]: grid1.append(1)
        else: grid1.append(0)
        if security[i] <= security[i+1]: grid2.append(1)
        else: grid2.append(0)

      start = 0
      for i in range(len(grid1)):
        start += grid1[i]
        grid1[i] = start

      start = 0
      for i in range(len(grid2)):
        start += grid2[i]
        grid2[i] = start

      res = []

      for t in range(time+1, len(grid1)-time):
        if grid1[t] - grid1[t-time] == time and grid2[t+time] - grid2[t] == time:
          res.append(t-1)

      return res