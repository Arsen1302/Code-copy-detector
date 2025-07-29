class Solution:
    def solution_1552_5(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end = [] , []                                          # start, end record the day that flower bloom/wither  
        res = []
        for s, e in flowers:
            start.append(s)
            end.append(e)
            
        start.sort()
        end.sort()
        
        for p in persons:
            flower = bisect_right(start, p) - bisect_left(end, p)    # The former will return how many flowers bloom before(include) day-p,
            res.append(flower)                                       # and the later will return how many flowers wither before(not-include) day-p,                                              
        
        return res