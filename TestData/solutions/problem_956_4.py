1st Solution
Time complexity - O(n)
Space complexity - O(n)

class Solution:
    def solution_956_4(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res, richest = [None] * n, max(candies)
        for i in range(n):
            res[i] = candies[i] + extraCandies >= richest
        return res

2nd Solution
Time complexity - O(n)
Space complexity - O(1)

class Solution:
    def solution_956_4(self, candies: List[int], extraCandies: int) -> List[bool]:
        richest = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= richest
        return candies