class Solution:
    def solution_1137_4(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            f = True
            for j in set(i):
                if(j not in allowed):
                    f = False
                    break
                    
            if(f):
                count += 1
        
        return count