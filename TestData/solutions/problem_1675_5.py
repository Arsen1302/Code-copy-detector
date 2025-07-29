class Solution:
    def solution_1675_5(self, names: List[str], heights: List[int]) -> List[str]:
        comb = zip(names,heights)
        res = []
        comb = sorted(comb, key =lambda x: x[1],reverse=True)
        for i in comb:
            res.append(i[0])
        return res