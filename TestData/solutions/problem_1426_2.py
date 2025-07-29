class Solution:
    def solution_1426_2(self, street: str) -> int:
        
        patterns = ['H.H', '.H', 'H.', 'H'] # 4 patterns (excluding '.' cuz it costs 0 )
        costs = [1, 1, 1, -1] # corresponding costs
        res = 0
        for p, c in zip(patterns, costs): # firstly, detect 'H.H'; secondly, detect '.H' and 'H.'; ...
            t = street.count(p) # occurences
            if (t >= 1):
                if (c == -1):  # if found an impossible case...
                    return -1
                res += c * t # accumulate the cost
                street = street.replace(p, '#') # erase such arrangement
        return res