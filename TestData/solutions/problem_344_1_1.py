class Solution:
    def solution_344_1_1(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        @cache
        def solution_344_1_2(i, j): # find longest common subsequence
            if i==m or j==n:
                return 0            
            return 1 + solution_344_1_2(i+1, j+1) if word1[i]==word2[j] else  max(solution_344_1_2(i+1, j), solution_344_1_2(i,j+1))                               
        # subtract the solution_344_1_2 length from both the strings 
        # the difference is the number of characters that has to deleted
        return m + n - 2*solution_344_1_2(0,0)