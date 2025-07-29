class Solution:
    def solution_1201_1(self, word1: str, word2: str) -> str:
        
        res=''
        
        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]