class Solution:
    def solution_958_2(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        i = 0

        while i<len(s1):
            if s1[i]>=s2[i]:
                i+=1
            else:
                break
        if i==len(s1):
            return True
            
        i = 0
        while i<len(s2):
            if s2[i]>=s1[i]:
                i+=1
            else:
                break
        if i==len(s2):
            return True
        return False