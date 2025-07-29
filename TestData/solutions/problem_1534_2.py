class Solution:
    def solution_1534_2(self, matches: List[List[int]]) -> List[List[int]]:
        winners=[x for (x,y) in matches]
		losers=[y for (x,y) in matches]
        perfect_winners=list(set(winners)-set(losers))
        C=Counter(losers) ; one_lost=[loser for loser in C if C[loser]==1]
        return [sorted(perfect_winners), sorted(one_lost)]