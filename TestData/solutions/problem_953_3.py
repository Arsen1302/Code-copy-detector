class Solution:
    def solution_953_3(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        
        maximumScore = max(cardPoints[0] + self.solution_953_3(cardPoints[1:], k - 1), cardPoints[n - 1] + self.solution_953_3(cardPoints[:n - 1], k - 1))
        return maximumScore