class Solution:
    def solution_341_5(self, candyType: List[int]) -> int:
        if len(candyType) / 2 >= len(set(candyType)):
            return len(set(candyType))
        else:
            return int(len(candyType) / 2)
       
            ```