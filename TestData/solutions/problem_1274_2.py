class Solution:
    def solution_1274_2(self, s: str, minJump: int, maxJump: int) -> bool:
        queue, lo = [0], 0
        for x in queue: 
            if x == len(s)-1: return True 
            for xx in range(max(lo+1, x+minJump), min(x+maxJump+1, len(s))): 
                if s[xx] == "0": queue.append(xx)
            lo = max(lo, x + maxJump)
        return False