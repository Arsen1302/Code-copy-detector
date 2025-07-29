class Solution:
    def solution_906_2(self, votes: List[str]) -> str:
        ranking = dict()
        for vote in votes: 
            for i, x in enumerate(vote): 
                ranking.setdefault(x, [0]*len(vote))[i] += 1
        return "".join(sorted(sorted(vote), key=ranking.get, reverse=True))