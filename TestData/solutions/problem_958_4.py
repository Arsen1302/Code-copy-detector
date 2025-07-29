class Solution:
    def solution_958_4(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
         
        f1, f2 = False, False
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            
            if not f1 and not f2:
                if s1[i] < s2[i]:
                    f2 = True
                else:
                    f1 = True
            
            if s1[i] < s2[i] and f1 or s1[i] > s2[i] and f2:
                return False
                
        
        return True