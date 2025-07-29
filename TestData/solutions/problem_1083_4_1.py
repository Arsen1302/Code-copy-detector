class Solution:
    def solution_1083_4_1(self, keyName: List[str], keyTime: List[str]) -> List[str]:
      def solution_1083_4_2(time):
        hour, minutes = int(time[:2]), int(time[3:])
        return hour*60 + minutes
      
      dicts = defaultdict(list)
      
      for i in range(len(keyName)):
        name, time = keyName[i], keyTime[i]
        dicts[name].append(solution_1083_4_2(time))
      
      res = []
      
      for key,value in dicts.items():
        value.sort()
        for t in range(len(value)-2):
          if value[t+2] - value[t] <= 60:
            res.append(key)
            break
            
      return sorted(res)