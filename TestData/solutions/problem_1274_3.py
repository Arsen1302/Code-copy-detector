class Solution:
    def solution_1274_3(self, s: str, minJump: int, maxJump: int) -> bool:
        lo = 0 
        can = [1] + [0]*(len(s)-1)
        for i, x in enumerate(s): 
            if x == "0" and can[i]: 
                for ii in range(max(lo+1, i+minJump), min(i+maxJump+1, len(s))): 
                    if s[ii] == "0": can[ii] = 1
                    lo = max(lo, i+maxJump) # key to pass 
        return can[len(s)-1]