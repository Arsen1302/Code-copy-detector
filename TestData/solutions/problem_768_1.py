class Solution:
    def solution_768_1(self, text1: str, text2: str) -> int:
        
        dp = []
        
        # Fill the matrix
        for _ in range(len(text1)+1):
            row = []
            for _ in range(len(text2)+1):
                row.append(0)
            
            dp.append(row)
        
        
        longest_length = 0
        
        # Start looping throught the text1 and text2
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                
                # If characters match
				# fill the current cell by adding one to the diagonal value
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # If characters do not match
					# Fill the cell with max value of previous row and column
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                # Keep track of the MAXIMUM value in the matrix
                longest_length = max(longest_length, dp[i][j])
        
        return longest_length