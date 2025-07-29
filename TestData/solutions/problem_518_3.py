class Solution(object):
    def solution_518_3(self, s):
        streak, out = 0, []
        
        for i in range(len(s)):
            streak += 1
            
            if i == len(s)-1 or s[i] != s[i+1]:
                if streak >= 3:
                    out.append([i-streak+1, i])
                    
                streak = 0
        
        return out