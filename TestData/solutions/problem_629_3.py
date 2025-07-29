class Solution:
    def solution_629_3(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0, len(tokens)-1
        curr_score = 0
        max_score = 0
        while l <= r:
            if(tokens[l] <= power):
                power -= tokens[l]
                curr_score += 1
                l += 1
                max_score = max(max_score, curr_score)
            elif(curr_score > 0):
                power += tokens[r]
                curr_score -= 1
                r -= 1
                max_score = max(max_score, curr_score)
            else:
                break
        return max_score