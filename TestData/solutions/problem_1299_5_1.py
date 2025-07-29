class Solution:
      
    def solution_1299_5_1(self, startTime: str, finishTime: str) -> int:
        res = 0
        if startTime > finishTime:
          res += self.solution_1299_5_2(startTime, '24:00')
          res += self.solution_1299_5_2('00:00', finishTime)
        else:
          res += self.solution_1299_5_2(startTime, finishTime)
        return res
  
    def solution_1299_5_2(self, start, end):
          start_hour, _   = [int(x) for x in start.split(':')]
          end_hour, _     = [int(x) for x in end.split(':')]
          count = 0
          for current_hour in range(start_hour, end_hour+1):
            quarters = [0, 15, 30, 45, 60]
            for i in range(len(quarters) - 1):
              first_q  = '%02d:%02d' % (current_hour, quarters[i])
              second_q = '%02d:%02d' % (current_hour, quarters[i+1])
              # 00:00 <= 00:15 <= 23:59 and 00:00 <= 00:30 <= 23.59
              if (start <= first_q <= end) and (start <= second_q <= end):
                count += 1
          return count