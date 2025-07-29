class Solution:
    def solution_344_5_1(self, word1: str, word2: str) -> int:
        
        
        memo = {}
        
        def solution_344_5_2(a,b):
            
            if a==len(word1):
                return len(word2)-b
            elif b==len(word2):
                return len(word1)-a
            elif (a,b) in memo:
                return memo[(a,b)]
            
            if word1[a] == word2[b]:
                memo[(a,b)] =solution_344_5_2(a+1,b+1) 
                return solution_344_5_2(a+1,b+1)
            else:
                memo[(a,b)] = 1+min(solution_344_5_2(a+1,b), solution_344_5_2(a,b+1))
                return 1+min(solution_344_5_2(a+1,b), solution_344_5_2(a,b+1))
        
            
            
        return solution_344_5_2(0,0)