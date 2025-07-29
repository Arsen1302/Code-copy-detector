class Solution:
    def solution_597_1(self, deck: List[int]) -> bool:
        x = Counter(deck).values()
        return reduce(gcd, x) > 1