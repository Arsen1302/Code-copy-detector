class Solution:
    def solution_1317_4(self, s: str) -> int:
        
        ctr = 0
        
        for i in range(97,123):
        
            first = s.find(chr(i))
            
            if f!=-1:
                last = s.rfind(chr(i))
                ctr += len(set(s[first+1:last])) # count of unique characters between first and last character
    
        return ctr