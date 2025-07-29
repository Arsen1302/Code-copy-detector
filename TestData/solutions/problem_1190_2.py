class Solution:
    def solution_1190_2(self, a: int, b: int, c: int) -> int:
        d = sorted([a,b,c])
        r = 0
        while len(d)>1: # continue removing stones when we have more than one piles
            d[0], d[-1] = d[0] - 1, d[-1] - 1   # removing stones from first and last piles
            if len(d) > 0 and d[-1]==0: # check if the last pile is empty
                d = d[:-1]
            if len(d) > 0 and d[0]==0: # check if the first pile is empty
                d = d[1:]
            r += 1  # increasing score after each step
            d = sorted(d)  # sort piles by stones
        return r