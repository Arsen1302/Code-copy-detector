class Solution:
    def solution_768_5_1(self, text1: str, text2: str) -> int:
        
        @cache
        def solution_768_5_2(i, j):
            
            if i == -1 or j == -1:
                # Any string compare to empty string has no common sequence
                return 0
            
            elif text1[i] == text2[j]:
                # Current character is the same
                return solution_768_5_2(i-1, j-1) + 1
            
            else:
                # Current characters are different
                return max( solution_768_5_2(i-1, j), solution_768_5_2(i, j-1) )
            
        # -------------------------------------------------
        return solution_768_5_2( len(text1)-1, len(text2)-1 )