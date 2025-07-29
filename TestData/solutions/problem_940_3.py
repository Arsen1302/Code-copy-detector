class Solution:
    def solution_940_3(self, words: List[str]) -> List[str]:
        
        wd = sorted(words, key=len)
        res = []
        
        for i in range(len(wd)):
            for j in range(i+1,len(wd)):
                if wd[i] in wd[j]:
                    res.append(wd[i])
                    break
                    
                    
        return res