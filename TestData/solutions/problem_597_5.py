class Solution:
    def solution_597_5(self, deck):
        return reduce(gcd, Counter(deck).values()) >= 2