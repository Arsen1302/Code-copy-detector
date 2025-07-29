class Solution(object):
    def solution_518_1(self, s):
        s += " "
        
        streak, char, out = 0, s[0], []
        
        for i,c in enumerate(s):
            if c != char:
                if streak >= 3:
                    out.append([i-streak, i-1])
                
                streak, char = 0, s[i]
                
            streak += 1
        
        return out