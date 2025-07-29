class Solution:
    def solution_956_5(self, candies: List[int], extraCandies: int) -> List[bool]:
        minRequiredCandies = max(candies) - extraCandies
        for idx, kid in enumerate(candies):
            candies[idx] = kid >= minRequiredCandies
        return candies