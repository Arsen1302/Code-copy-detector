class Solution:
    def solution_1524_1(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        # Initialization with round 1 (round 0 is skipped)
        dp = {(0, 0): (0, numArrows), (0, aliceArrows[1] + 1): (1, numArrows - (aliceArrows[1] + 1))}
        
        # Loop from round 2
        for i in range(2, 12):
            prev = dp
            dp = {}
            
            # Consider two possible strategies for each state from last round: to bid and not to bid
            for key in prev:
                
                # Base case: not to bid in this round. Score and arrows left do not change.
                # Simply append 0 at the end to the key.
                newkey1 = list(key)
                newkey1.append(0)
                score, arrowleft = prev[key]
                
                newval1 = (score, arrowleft)
                dp[tuple(newkey1)] = newval1
                
                # If we still have enough arrows, we can bid in this round
                if arrowleft >= aliceArrows[i] + 1:
                    newkey2 = list(key)
                    newkey2.append(aliceArrows[i] + 1)
                    newval2 = (score + i, arrowleft - (aliceArrows[i] + 1))
                    dp[tuple(newkey2)] = newval2
        
        # Select the bidding history with max score
        maxscore, res = 0, None
        for key in dp:
            score, _ = dp[key]
            if score > maxscore:
                maxscore = score
                res = list(key)
        
        # Taking care of the corner case, where too many arrows are given
        if sum(res) < numArrows:
            res[0] = numArrows - sum(res)
        
        return res