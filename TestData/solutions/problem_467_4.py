class Solution:
    def solution_467_4(self, start: str, end: str) -> bool:
        if Counter(start) != Counter(end): return False # edge case 
        fs = fe = bs = be = 0 # forward s &amp; e counter and backward s &amp; e counter 
        for i in range(len(start)): 
            fs = 0 if start[i]  == "L" else (fs + start[i] == "R")
            fe = 0 if end[i]    == "L" else (fs + end[i] == "R")
            bs = 0 if start[~i] == "R" else (bs + start[~i] == "L")
            be = 0 if end[~i]   == "R" else (be + end[~i] == "L")
            if fs < fe or bs < be: return False
        return True