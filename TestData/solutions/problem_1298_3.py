class Solution:
    def solution_1298_3(self, num: str) -> str:
        ii = -1
        for i, x in enumerate(num): 
            if int(x) &amp; 1: ii = i 
        return num[:ii+1]