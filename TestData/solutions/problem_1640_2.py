class Solution:
    def solution_1640_2(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        
        for i, val in enumerate(edges):
            score[val] += i
        return score.index(max(score))