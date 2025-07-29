class Solution:
    def solution_494_1(self, widths: List[int], s: str) -> List[int]:
        count = ans =  wi = 0
        s = list(s)
        while s:
            val = ord(s[0]) - 97
            
            if(widths[val] + wi > 100):
                wi = 0
                count += 1
            
            wi += widths[val]
            
            s.pop(0)
        return([count + 1 , wi])