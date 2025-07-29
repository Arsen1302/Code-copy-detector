class Solution(object):
    def solution_518_4(self, s):
        start, out = 0, []
        
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                if i-start+1 >= 3:
                    out.append([start, i])
                
                start = i+1
        
        return out