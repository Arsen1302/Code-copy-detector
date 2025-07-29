class Solution:
    def solution_1206_4(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        q = [target - basecost for basecost in baseCosts]

        for toppingcost in toppingCosts:
            q += [val - cost for val in q if val > 0 for cost in (toppingcost, toppingcost * 2)]

        return target - min(q, key=lambda x: abs(x) * 2 - (x > 0))