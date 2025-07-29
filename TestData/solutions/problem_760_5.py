class Solution:
    def solution_760_5(self, dominoes: List[List[int]]) -> int:
        # To calculate:
        # - Image a bunch of equivalent pairs as a graph with edges between every node.
        # 2 -> 1
        # 3 -> 2 + 1 = 2
        # 4 -> 3 + 2 + 1 = 6
        # i.e. (n - 1) * n // 2
        d = Counter((min(x, y), max(x, y)) for x, y in dominoes)
        return sum((v - 1) * v // 2 for v in d.values())