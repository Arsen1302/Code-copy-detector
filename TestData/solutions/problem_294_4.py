class Solution:
    def solution_294_4(self, score: List[int]) -> List[str]:
        x = sorted(score, reverse=True)
        d = {}
        for i,j in enumerate(x):
            if i == 0:
                d[j] = "Gold Medal"
            elif i == 1:
                d[j] = "Silver Medal"
            elif i == 2:
                d[j] = "Bronze Medal"
            else:
                d[j] = str(i+1)
        return [d[i] for i in score]