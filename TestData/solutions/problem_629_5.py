class Solution:
    def solution_629_5(self, tokens: List[int], power: int) -> int:
        score, ans = 0, 0                           # variable initialization
        tokens.sort()                               # sorting it in non decreasing order
        n = len(tokens)
        i=0
        while i<n:
            if power < tokens[i]:                   # if power is less than tokens[i]
                if score > 0:                       # score > 0 means we can face down and increase the power
                    power += tokens[n-1]
                    n-=1
                    score -= 1                      # decreasing the score as used for increase in power
                else: i+=1
            else:
                power -= tokens[i]                  # decreasing the power as it used to increase the score
                score += 1                          # increasing the score
                i+=1
            ans = max(ans, score)                   # keep track of maximum score
        return ans