class Solution:
    def solution_865_5(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        [+][ ][ ][-]
        [ ][a][b][ ] 
        [ ][c][d][ ] dp[d] = dp[b] + dp[c] - dp[a] + mat[d]
        [-][ ][ ][+]
                                lower_right     upper_right     lower_left        upper_left
        block_sum[(i,j), k] = dp[i+k, j+k] - dp[i-k-1, j+k] - dp[i+k, j-k-1] - dp[i-k-1, j-k-1]
        """
        # dp[i][j] is the prefix sum of all elemnt before i, j
        dp = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # init dp
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                # init dp left &amp; upper border
                if i == 0 and j == 0:
                    dp[i][j] = mat[i][j]
                    continue
                elif i == 0:
                    dp[i][j] = mat[i][j] + dp[i][j-1]
                    continue
                elif j == 0:
                    dp[i][j] = mat[i][j] + dp[i-1][j]
                    continue
                    
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i][j]
        
        # for m in mat:
        #     print(m)
        # print("--------------")
        # for i in dp:
        #     print(i)
            
        res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # calculate block sum
        row_max = len(res) - 1
        col_max = len(res[0]) - 1
        for i in range(len(res)):
            for j in range(len(res[0])):
                lower_right = dp[min(i+k, row_max)][min(j+k, col_max)]
                upper_left = 0 if (i-k-1<0 or j-k-1<0) else dp[i-k-1][j-k-1]
                lower_left = 0 if (j-k-1<0) else dp[min(i+k, row_max)][j-k-1]
                upper_right = 0 if (i-k-1<0) else dp[i-k-1][min(j+k, col_max)]
                
                res[i][j] = lower_right - upper_right - lower_left + upper_left
                
        return res