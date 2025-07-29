class Solution:
    def solution_341_1(self, candyType: List[int]) -> int:
        return min(len(candyType) //2, len(set(candyType)))