class Solution:
    def solution_956_1(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [x+extraCandies >= max(candies) for x in candies]