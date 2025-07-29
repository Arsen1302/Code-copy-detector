class Solution:
    def solution_958_3(self, s1: str, s2: str) -> bool:
        
        s1, s2 = sorted(s1), sorted(s2)
        
        first = all([s1[i] >= s2[i] for i,_ in enumerate(s1)])
        
        return first if first else all([s1[i] <= s2[i] for i,_ in enumerate(s1)])