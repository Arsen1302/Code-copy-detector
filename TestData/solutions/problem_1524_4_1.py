class Solution:
    def solution_1524_4_1(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        # DP, table to store the max score for current section and number of arrows
        dp = [[-1 for _ in range(numArrows + 1)] for _ in range(12)]
        # minArrowsForBobToWin stores bob arrows to win in each section
        # bobMaxScore stores result bob arrows for max score
        minArrowsForBobToWin, bobMaxScore = [aliceArrows[i] + 1 for i in range(len(aliceArrows))], [0 for _ in range(12)]
        
        # Helper function to find max score for each number of arrows upto the actual number of arrows
        # for all the sections upto a given section
        def solution_1524_4_2(section: int, numArrows: int, dp: List[List[int]], minArrowsForBobToWin: List[int]) -> int:
            # base case
            # return score 0 for arrows <= 0 or section <= 0
            if numArrows <= 0 or section <= 0:
                return 0
            # returning precalculated result
            if dp[section][numArrows] != -1:
                return dp[section][numArrows]
            # Variables to store the scores if the current section is taken or not
            taken, notTaken = 0, 0
            # if remaining arrows >= minArrowsForBobToWin[section] then we can take current section 
            # and call recursively
            if numArrows >= minArrowsForBobToWin[section]:
                taken =  section + solution_1524_4_2(section - 1, numArrows - minArrowsForBobToWin[section], dp, minArrowsForBobToWin)
            # recursive call without taking current section
            notTaken = solution_1524_4_2(section - 1, numArrows, dp, minArrowsForBobToWin)
            # get max score from taken and not taken case
            dp[section][numArrows] = max(taken, notTaken)
            return dp[section][numArrows]
        
        # find maximum score bob can obtain
        solution_1524_4_2(11, numArrows, dp, minArrowsForBobToWin)
        # find bob's arrows for each section starting from max score section
        for i in range(11, 0, -1):
            if numArrows >= minArrowsForBobToWin[i] and dp[i][numArrows] > dp[i - 1][numArrows]:
                bobMaxScore[i] = minArrowsForBobToWin[i]
                numArrows -= minArrowsForBobToWin[i]
                if numArrows <= 0:
                    break
        # add remaining arrows in section 0
        if numArrows > 0:
            bobMaxScore[0] = numArrows
        return bobMaxScore