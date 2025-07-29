class Solution:
    def solution_1217_3(self, s1: str, s2: str) -> bool:
        size1, size2 = len(s1), len(s2)        
        if size1 != size2:
            return False
        
        pos1 = pos2 = -1
        for i in range(size1):
            if s1[i] != s2[i]:
                if pos1 == -1:
                    pos1 = i
                elif pos2 == -1:
                    pos2 = i
                else:
                    return False
        
        return (pos1 == -1 and pos2 == -1) or (pos1 != -1 and pos2 != -1 and s1[pos1] == s2[pos2] and s1[pos2] == s2[pos1])