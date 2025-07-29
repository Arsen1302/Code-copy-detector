class Solution:
    def solution_597_2(self, deck: List[int]) -> bool:
        return gcd(*Counter(deck).values())>1