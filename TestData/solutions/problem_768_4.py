class Solution:
    def solution_768_4(self, text1: str, text2: str) -> int:
        
        # padding one space for empty string representation
        text1 = ' ' + text1
        text2 = ' ' + text2

        w, h = len(text1), len(text2)

        dp_table = [ [ 0 for x in range(w) ] for y in range(h) ]

        # update dynamic programming table with optimal substructure
        for y in range(1, h):
            for x in range(1, w):

                if text1[x] == text2[y]:
                    # with the same character
                    # extend the length of common subsequence
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                
                else:
                    # with different characters
                    # choose the optimal subsequence
                    dp_table[y][x] = max( dp_table[y-1][x], dp_table[y][x-1] )

        return dp_table[-1][-1]