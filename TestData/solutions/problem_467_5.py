class Solution:
    def solution_467_5(self, start: str, end: str) -> bool:
        ss = [(x, i) for i, x in enumerate(start) if x != "X"]
        ee = [(x, i) for i, x in enumerate(end) if x != "X"]
        
        if len(ss) != len(ee): return False 
        
        for (s, i), (e, j) in zip(ss, ee): 
            if s != e: return False 
            if s == e == "L" and i < j: return False 
            if s == e == "R" and i > j: return False 
        return True