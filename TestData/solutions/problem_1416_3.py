class Solution:
    def solution_1416_3(self, items: List[List[int]], queries: List[int]) -> List[int]:
        max_beauty = defaultdict(int)
        for price, beauty in items:
            max_beauty[price] = max(beauty, max_beauty[price])
        prices = sorted(max_beauty.keys())
        for p1, p2 in zip(prices, prices[1:]):
            max_beauty[p2] = max(max_beauty[p2], max_beauty[p1])
        return [max_beauty[prices[idx - 1]]
                if (idx := bisect_right(prices, q)) > 0 else 0
                for q in queries]