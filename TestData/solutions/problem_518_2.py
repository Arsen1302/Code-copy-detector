class Solution(object):
    def solution_518_2(self, s):
        s += " "
        
        start, char, out = 0, s[0], []
        
        for i,c in enumerate(s):
            if c != char:
                if i-start >= 3:
                    out.append([start, i-1])
                
                start, char = i, s[i]
        
        return out